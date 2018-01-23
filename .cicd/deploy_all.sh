# Run from project root
echo Deploying toy celery pipelines with version $1

function cicd_get_id {
    cicd pipeline list $1 | jq '.pipelines[0].pipeline_id' | sed 's/\"//g'
}

cicd pipeline update `cicd_get_id toy-celery-broker-backend` --service .cicd/broker-backend/service.yaml --stages .cicd/broker-backend/stages.yaml
cicd pipeline deploy `cicd_get_id toy-celery-broker-backend`

sed -i '' "s/latest/$1/g" .cicd/beat/service.yaml
cicd pipeline update `cicd_get_id toy-celery-beat` --service .cicd/beat/service.yaml --stages .cicd/beat/stages.yaml
cicd pipeline deploy `cicd_get_id toy-celery-beat`
git checkout -- .cicd/beat/service.yaml

sed -i '' "s/latest/$1/g" .cicd/flower/service.yaml
cicd pipeline update `cicd_get_id toy-celery-flower` --service .cicd/flower/service.yaml --stages .cicd/flower/stages.yaml
cicd pipeline deploy `cicd_get_id toy-celery-flower`
git checkout -- .cicd/flower/service.yaml

sed -i '' "s/latest/$1/g" .cicd/worker/service.yaml
cicd pipeline update `cicd_get_id toy-celery-worker` --service .cicd/worker/service.yaml --stages .cicd/worker/stages.yaml
cicd pipeline deploy `cicd_get_id toy-celery-worker`
git checkout -- .cicd/worker/service.yaml

sed -i '' "s/latest/$1/g" .cicd/monitor/service.yaml
cicd pipeline update `cicd_get_id toy-celery-monitor` --service .cicd/monitor/service.yaml --stages .cicd/monitor/stages.yaml
cicd pipeline deploy `cicd_get_id toy-celery-monitor`
git checkout -- .cicd/monitor/service.yaml
