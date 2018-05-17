################################################################################
#
#			FOR CICD
#
################################################################################

ifndef RUN_MODE
	RUN_MODE = noop
endif

ifndef QUEUES
	queues = celery,goodbye
else
	queues = ${QUEUES}
endif

run: $(RUN_MODE)

noop:
	@echo "NO-OP"

create-pipelines:
	. .cicd/create_all.sh

delete-pipelines:
	. .cicd/delete_all.sh

deploy-pipelines: require-version docker
	docker tag jwplayer/toy-celery:local jwplayer/toy-celery:${version}
	docker push jwplayer/toy-celery:${version}
	. .cicd/deploy_all.sh ${version}

require-version:
ifndef version
	$(error This command requires a "version" argument specified like this: "version=<version>")
endif

################################################################################
#
#			FOR STARTING THE APP
#			TODO: convert this section to a shell script
#
################################################################################

worker:
	@echo "STARTING TOY APP WORKER WITH QUEUES ${queues}" \
		&& celery worker -A toy_app.app -Q ${queues} --concurrency 1

beat:
	celery beat -A toy_app.app -l info

flower:
	celery flower -A toy_app.app

################################################################################
#
#			FOR DEVELOPMENT
#
################################################################################

build: clean
	docker-compose build

run-local: clean
	docker-compose up -d
	docker-compose logs -f -t

install:
	python setup.py install

clean:
	docker-compose down
	rm -rf *.pyc
	rm -rf celerybeat*
