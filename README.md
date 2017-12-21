# Toy Celery

This is a barebones celery setup. Includes: 
1. A task running on default queue, a task running on a different queue (`worker/task.py`)
1. Beat schedule (`worker/schedule.py`)
1. Celery app instance (`worker/app.py`) that imports the tasks and schedule
1. Makefile entrypoint for starting worker, beat, flower
1. Alpine-based Dockerfile
1. Docker Compose file to build and run the setup locally
1. CICD pipeline configurations for broker, worker, beat, flower (`.cicd`)
