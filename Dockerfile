FROM alpine:3.5

RUN apk add --no-cache \
        musl \
        build-base \
        linux-headers \
        ca-certificates \
        python2 \
        python2-dev \
        py-setuptools && \
    rm -rf /var/cache/apk/*

COPY . /srv/
WORKDIR /srv

RUN /usr/bin/easy_install-2.7 pip && \
    pip install --upgrade pip && \
    make install

EXPOSE 8000

# TODO: change to a shell script that execs the process that we want to start
# This is actually a bad practice - we want the service to be PID 1 to
# so the container can properly handle unix signals
CMD ["make", "run"]
