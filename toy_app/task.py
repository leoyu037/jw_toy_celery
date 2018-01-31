import os

from celery import shared_task
import redis


@shared_task(name='print.hello')
def hello():
    print '{}: Hello World!'.format(os.environ.get('HOSTNAME'))


@shared_task(name='print.goodbye')
def goodbye():
    print '{}: Goodbye cruel world!'.format(os.environ.get('HOSTNAME'))


@shared_task(name='heartbeat', bind=True)
def heartbeat(self):
    r = redis.StrictRedis(host='toy-celery-broker-backend', port=6379, db=0)

    for queue in ['celery', 'goodbye', 'buildup']:
        print 'Queue {} size: {}'.format(queue, r.llen(queue))
