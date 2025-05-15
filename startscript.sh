#!/bin/bash
set -euo pipefail

log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

log "Initializing Airflow DB..."
airflow db upgrade

log "Parsing DAGs..."
airflow scheduler --num-runs 1

DAG_ID="spacex_etl_dag"

log "Creating admin user (if not exists)..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# 🚀 Only trigger DAG if running inside scheduler
if [[ "$1" == "scheduler" ]]; then
  log "Triggering DAG: $DAG_ID"
  airflow dags trigger "$DAG_ID"
fi

if [[ "$1" == "webserver" || "$1" == "scheduler" ]]; then
  log "Starting Airflow: $1"
  exec airflow "$@"
else
  log "Executing: $@"
  exec "$@"
fi