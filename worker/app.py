

from celery import Celery

from schedule import CELERYBEAT_SCHEDULE

broker = 'redis://toy-celery-broker-backend:6379//0'
app = Celery('tasks',
    broker=broker,
    # necessary for celery.shared_task tasks
    include=['worker.task']
)
app.conf.update(
    CELERYBEAT_SCHEDULE=CELERYBEAT_SCHEDULE
)
