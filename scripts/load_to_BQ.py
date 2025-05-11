import logging
from google.cloud import bigquery
import os

# Set your service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/opt/airflow/secrets/llms-395417-c18ea70a3f54.json"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------- STEP 1: Load CSV to BigQuery --------------------
def load_csv_to_bigquery():

    project_id = "llms-395417"
    dataset_id = "spacex_dataset"         # Existing BigQuery dataset
    table_id = "spacex_table"             # Desired table name
    gcs_uri = "gs://shwetabucket/raw/spacex_launches.csv"  # Path to your uploaded csv file

    # Initialize the BigQuery client
    client = bigquery.Client(project=project_id)

    # Construct full table reference
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    # Set up the job configuration
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    try:

        # Start the load job
        load_job = client.load_table_from_uri(
            gcs_uri,
            table_ref,
            job_config=job_config
        )

        # Wait for the job to complete
        load_job.result()

        # Confirm the result
        logging.info(f"✅ Loaded {load_job.output_rows} rows into {table_ref}")

    except Exception as e:
        logging.info(f"Failed to load data to BQ: {e}")
# -------------------- RUN --------------------

if __name__=="__main__":

    logging.info("Loading CSV to BQ")
    load_csv_to_bigquery()
    logging.info("Successfully loaded data to table in BQ!!")
