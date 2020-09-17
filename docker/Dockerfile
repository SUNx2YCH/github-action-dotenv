FROM alpine:edge

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk --no-cache add \
        micropython

COPY action.py /action.py
ENTRYPOINT ["/action.py"]
