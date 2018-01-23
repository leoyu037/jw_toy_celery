# Run from project root
echo Creating toy celery pipelines...

cicd pipeline create --service-name toy-celery-broker-backend --description "Toy Celery Broker/Backend" --service .cicd/broker-backend/service.yaml --stages .cicd/broker-backend/stages.yaml

cicd pipeline create --service-name toy-celery-beat --description "Toy Celery Beat" --service .cicd/beat/service.yaml --stages .cicd/beat/stages.yaml

cicd pipeline create --service-name toy-celery-flower --description "Toy Celery Flower" --service .cicd/flower/service.yaml --stages .cicd/flower/stages.yaml

cicd pipeline create --service-name toy-celery-worker --description "Toy Celery Worker" --service .cicd/worker/service.yaml --stages .cicd/worker/stages.yaml

cicd pipeline create --service-name toy-celery-monitor --description "Toy Celery Monitor" --service .cicd/monitor/service.yaml --stages .cicd/monitor/stages.yaml
