# Toy Celery

This is a barebones celery setup. Includes:
1. A task running on default queue, a task running on a different queue (`worker/task.py`)
1. Beat schedule (`worker/schedule.py`)
1. Celery app instance (`worker/app.py`) that imports the tasks and schedule
1. Makefile entrypoint for starting worker, beat, flower
1. Alpine-based Dockerfile
1. Docker Compose file to build and run the setup locally
1. (JW Player specific) CICD pipeline configurations for broker, worker, beat, flower (`.cicd`)

-----------

## Requirements
1. Docker
1. Docker Compose
1. (For deploying to JW Player CICD) CICD-CLI and a Dockerhub account

## Starting the application locally
```bash
  # Build image
  make docker

  # Start app
  make docker-compose
```

## Deploying to JW Player CICD
```bash
  # Log in to Dockerhub
  docker login

  # Build docker image, push to Dockerhub, deploy to CICD
  make deploy-pipelines version=<version>
```
