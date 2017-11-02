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
    pip install celery redis flower && \
    make install

EXPOSE 8000

CMD ["make", "run"]
