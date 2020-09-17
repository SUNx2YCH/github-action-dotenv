#!/usr/bin/env micropython

import os
import re
import sys

dotenv_file = sys.argv[1]

try:
    os.stat(dotenv_file)
except OSError:
    print('::error::File not found: {file!r}'.format(file=dotenv_file))
    sys.exit(1)

with open(dotenv_file) as fp:
    for line in fp.readlines():
        # https://docs.docker.com/compose/env-file/#syntax-rules
        if line.startswith('#') or not line.strip():
            continue
        match = re.match(r'^([^=]+)=(.*)$', line)
        if match:
            print('::set-env name={name}::{value}'.format(name=match.group(1), value=match.group(2)))
        else:
            print('::warning::Wrong syntax: {line!r}'.format(line=line))
