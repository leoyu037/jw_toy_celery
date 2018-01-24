import os
import sys

# Add path for docker
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

from toy_app import dd


def monitor(app):
    """Monitor celery application."""
    state = app.events.State(max_tasks_in_memory=500)

    def datadog_test_during_task(event):
        print('during task. success:12, failed:7')
        dd.increment_counter('toy_celery.datadog_test.monitor_during_task',
            value=12, tags=['status:success'])
        dd.increment_counter('toy_celery.datadog_test.monitor_during_task',
            value=7, tags=['status:failed'])

    def datadog_test_after_task(event):
        print('after task. success:13, failed:8')
        dd.increment_counter('toy_celery.datadog_test.monitor_after_task',
            value=13, tags=['status:success'])
        dd.increment_counter('toy_celery.datadog_test.monitor_after_task',
            value=8, tags=['status:failed'])

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
            'datadog-test-during-task': datadog_test_during_task,
            'datadog-test-after-task': datadog_test_after_task,
            '*': state.event,
        })
        recv.capture(limit=None, timeout=None, wakeup=True)


if __name__ == '__main__':  # run monitor
    from toy_app.app import app

    print('Starting Toy Celery monitor')
    monitor(app)
