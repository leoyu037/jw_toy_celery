ifeq ($(RUN_MODE),cowboy_mode)
	CMD := cowboy
else
	ifeq ($(RUN_MODE),beat)
		CMD := beat
	else
		ifeq ($(RUN_MODE),flower)
			CMD := flower
		else
			ifeq ($(RUN_MODE),hello)
				CMD := hello-worker
			else
				ifeq ($(RUN_MODE),goodbye)
					CMD := goodbye-worker
				else
					CMD := worker
				endif
			endif
		endif
	endif
endif

run: $(CMD)

cowboy:
	@echo "wooooah nelly"

install:
	python setup.py install

clean:
	rm -rf *.pyc

PHONY=worker
worker::
	celery worker -A worker.app -Q celery,goodbye --concurrency 1

beat-worker:
	celery worker -A worker.app -Q celery,goodbye -B --concurrency 1

hello-worker:
	celery worker -A worker.app -Q celery --concurrency 1

goodbye-worker:
	celery worker -A worker.app -Q goodbye --concurrency 1

beat:
	celery beat -A worker.app -l info

flower:
	celery flower -A worker.app
