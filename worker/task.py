from datetime import timedelta
import os

# from billiard import current_process
from celery import Celery

broker = 'redis://toy-celery-broker-backend:6379//0'
app = Celery('tasks', broker=broker)

app.conf.beat_schedule = {
    # Running in default 'celery' queue
    'hello-every-5s': {
        'task': 'tasks.hello',
        'schedule': timedelta(seconds=5),
    },

    # Running in a different queue
    'goodbye-every-5s': {
        'task': 'print.goodbye',
        'schedule': timedelta(seconds=5),
        'options': {'queue': 'goodbye'},
    },
}


@app.task(name='tasks.hello')
def hello():
    print '{}: Hello World!'.format(os.environ.get('HOSTNAME'))


@app.task(name='print.goodbye')
def goodbye():
    print '{}: Goodbye cruel world!'.format(os.environ.get('HOSTNAME'))
