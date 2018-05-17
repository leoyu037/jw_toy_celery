from setuptools import setup

setup(
    name='jw-toy-celery',
    version='0.0.1',
    # packages=['toy_app'],
    install_requires=[
        'celery',
        'flower',
        'redis',
    ],
)
