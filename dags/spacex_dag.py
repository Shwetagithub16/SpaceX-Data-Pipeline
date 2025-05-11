from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import warnings
import os
import sys

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

# Now you can import from scripts
from scripts import extract_and_gcpload, load_to_BQ

default_args = {
    'owner': 'shweta',
    'start_date': datetime(2025, 4, 24),
    'retries': 0
}

with DAG(
    'spacex_etl_dag',
    default_args=default_args,
    schedule_interval=None,
    schedule=None,
    catchup=False              #prevents Airflow from running missed periods
) as dag:

    extract_and_upload = PythonOperator(
        task_id="extract_and_upload_to_gcs",
        python_callable=extract_and_gcpload.load_to_gcp_pipeline,
    )

    load_to_bq = PythonOperator(
        task_id="load_to_BQ",
        python_callable=load_to_BQ.load_csv_to_bigquery
    )

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command='dbt run --project-dir /opt/airflow/dbt/my_dbt --profiles-dir /opt/airflow/dbt'
    )

    extract_and_upload >> load_to_bq >> run_dbt
