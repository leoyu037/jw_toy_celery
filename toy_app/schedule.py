from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    # Running in default 'celery' queue
    'hello-every-5s': {
        'task': 'print.hello',
        'schedule': 5,  # 5s
    },

    # Running in a different queue
    'goodbye-every-5s': {
        'task': 'print.goodbye',
        'schedule': timedelta(seconds=5),  # another way to specify frequency
        'options': {'queue': 'goodbye'},
    },

    # Heartbeat
    'heartbeat-every-5s': {
        'task': 'heartbeat',
        'schedule': 5,
    },

    # No workers servicing this queue
    'queue-buildup': {
        'task': 'print.goodbye',
        'schedule': 1,
        'options': {'queue': 'buildup'},
    },
}
