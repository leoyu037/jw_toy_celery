from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    # Running in default 'celery' queue
    'hello-every-5s': {
        'task': 'tasks.hello',
        'schedule': 5,  # 5s
    },

    # Running in a different queue
    'goodbye-every-5s': {
        'task': 'print.goodbye',
        'schedule': timedelta(seconds=5),
        'options': {'queue': 'goodbye'},
    },
}
