import os

# from billiard import current_process

from celery import shared_task


@shared_task(name='tasks.hello')
def hello():
    print '{}: Hello World!'.format(os.environ.get('HOSTNAME'))


@shared_task(name='print.goodbye')
def goodbye():
    print '{}: Goodbye cruel world!'.format(os.environ.get('HOSTNAME'))
