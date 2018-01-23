# Run from project root
echo Delete toy celery pipelines...

function cicd_get_id {
    cicd pipeline list $1 | jq '.pipelines[0].pipeline_id' | sed 's/\"//g'
}

cicd pipeline delete `cicd_get_id toy-celery-broker-backend`

cicd pipeline delete `cicd_get_id toy-celery-beat`

cicd pipeline delete `cicd_get_id toy-celery-flower`

cicd pipeline delete `cicd_get_id toy-celery-worker`

cicd pipeline delete `cicd_get_id toy-celery-monitor`
