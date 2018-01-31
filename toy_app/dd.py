"""Datadog utility functions."""
import os

from datadog import DogStatsd

ENV = os.environ.get('ENV', 'LOCAL')
STATSD_HOST = os.environ.get('DOGSTATSD_SERVICE_HOST', 'localhost')
BASE_TAGS = ['application:toy_celery', 'env:{}'.format(ENV)]

statsd = DogStatsd(host=STATSD_HOST)


def _get_tags(additional_tags=None):
    return BASE_TAGS + additional_tags if additional_tags else BASE_TAGS


def send_event(title, text, alert_type='info', tags=None):
    statsd.event(title=title, text=text, tags=_get_tags(tags),
                 alert_type=alert_type)


def send_gauge(metric, value, tags=None):
    statsd.gauge(metric=metric, value=value, tags=_get_tags(tags))


def increment_counter(metric, value=1, tags=None):
    statsd.increment(metric, value=value, tags=_get_tags(tags))


def histogram(*args, **kwargs):
    tags = kwargs.pop('tags', None)
    statsd.histogram(tags=_get_tags(tags), *args, **kwargs)
