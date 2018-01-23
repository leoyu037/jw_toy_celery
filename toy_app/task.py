import os

from celery import shared_task, Task, current_app

from toy_app import dd
from toy_app.log import logger


@shared_task(name='print.hello')
def hello():
    print '{}: Hello World!'.format(os.environ.get('HOSTNAME'))


@shared_task(name='print.goodbye')
def goodbye():
    print '{}: Goodbye cruel world!'.format(os.environ.get('HOSTNAME'))


def emit_event(event, result):
    """ Emit custom celery event """
    logger.info('{}: {}'.format(event, result))
    with current_app.events.default_dispatcher() as dispatcher:
        dispatcher.send(event, result=result)


class DatadogTest(Task):
    """ Test datadog metrics """

    name = 'tasks.datadog_test'

    def run(self):
        logger.info('Datadog test. '
            'Incrementing counter toy_celery.datadog_test.during_task '
            'success: 10, failed: 5')
        dd.increment_counter('toy_celery.datadog_test.during_task',
            value=10, tags=['status:success'])
        dd.increment_counter('toy_celery.datadog_test.during_task',
            value=5, tags=['status:failed'])

        emit_event('datadog-test-during-task', 'Datadog test during task')

    def on_success(self, retval, task_id, args, kwargs):
        logger.info('Datadog test. '
            'Incrementing counter toy_celery.datadog_test.after_task '
            'success: 11, failed: 6')
        dd.increment_counter('toy_celery.datadog_test.after_task',
            value=11, tags=['status:success'])
        dd.increment_counter('toy_celery.datadog_test.after_task',
            value=6, tags=['status:failed'])

        emit_event('datadog-test-after-task', 'Datadog test after task')
