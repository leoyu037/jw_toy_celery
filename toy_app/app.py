

from celery import Celery
from celery.signals import task_prerun, celeryd_after_setup, celeryd_init, \
    worker_init, worker_ready, worker_process_init

from toy_app.schedule import CELERYBEAT_SCHEDULE

broker_backend = 'redis://toy-celery-broker-backend:6379//0'
app = Celery(
    'toy_app',
    broker=broker_backend,
    backend=broker_backend,
    # necessary for celery.shared_task tasks
    include=['toy_app.task'],
)
app.conf.update(
    CELERYBEAT_SCHEDULE=CELERYBEAT_SCHEDULE
)


@task_prerun.connect
def task_prerun_handler(*args, **kwargs):
    print('task prerun')


@celeryd_after_setup.connect
def celeryd_after_setup_handler(*args, **kwargs):
    print('celeryd_after_setup')


@celeryd_init.connect
def celeryd_init_handler(*args, **kwargs):
    print('celeryd_init')


@worker_init.connect
def worker_init_handler(*args, **kwargs):
    print('worker_init')


@worker_ready.connect
def worker_ready_handler(*args, **kwargs):
    print('worker_ready')


@worker_process_init.connect
def worker_process_init_handler(*args, **kwargs):
    print('worker_process_init')
