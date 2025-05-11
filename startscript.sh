#!/bin/bash
set -euxo pipefail

log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

log "Initializing Airflow DB..."
airflow db upgrade

log "Listing available DAGs..."
airflow dags list

log "Creating admin user (if not exists)..."
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

DAG_ID="spacex_etl_dag"

log "Waiting for DAG '$DAG_ID' to be available..."
for i in {1..10}; do
  if airflow dags list | grep -q "$DAG_ID"; then
    log "DAG '$DAG_ID' found."
    break
  fi
  log "DAG '$DAG_ID' not found yet. Retrying ($i/10)..."
  sleep 5
done

# Final check to ensure DAG was found
if ! airflow dags list | grep -q "$DAG_ID"; then
  log "Error: DAG '$DAG_ID' not found after multiple retries."
  exit 1
fi

log "Triggering DAG: $DAG_ID"
airflow dags trigger "$DAG_ID" --conf '{}'

log "DAG trigger command issued. Exiting..."
