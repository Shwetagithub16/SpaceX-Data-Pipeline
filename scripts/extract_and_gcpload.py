import requests
import json
from google.cloud import storage
import os
import logging
import pandas as pd
from google.cloud.dataproc_v1 import LoggingConfig

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "llms-395417-c18ea70a3f54.json"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_data_from_url():
    url = "https://api.spacexdata.com/v5/launches"
    try:
        response = requests.get(url)
        response.raise_for_status()
        jsondata = response.json()
        logging.info("✅ Successfully fetched launch data from SpaceX API")
        return jsondata
    except requests.exceptions.RequestException as e:
        logging.ERROR(f"Failed to fetch launch data:{e}")
        return []

def transform_data(rawdata):
        # ✅ Convert JSON array to newline-delimited JSON (NDJSON)
        logging.info("Transformaing Raw Data")

        launches=[]
        for launch in rawdata:
            details_clean = launch.get("details")
            if details_clean:
                # Remove problematic line breaks and extra quotes
                details_clean = details_clean.replace('\n', ' ').replace('\r', ' ').replace('"', "'")

            launches.append({
                "id": launch.get("id"),
                "name": launch.get("name"),
                "date_utc": launch.get("date_utc"),
                "success": launch.get("success"),
                "rocket": launch.get("rocket"),
                "details": details_clean,
                "flight_number": launch.get("flight_number")
            })

        df = pd.DataFrame(launches)
        logging.info("Transformed data to csv")
        return df


def load_to_gcp(df):

    try:
        # GCS upload config
        logging.info("Uploading data to GCP!")
        bucket_name = "shwetabucket"
        destination_blob_name = "raw/spacex_launches.csv"  # This is now csv

        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # ✅ Upload csv to GCS
        blob.upload_from_string(df.to_csv(index=False), 'text/csv')
        logging.info(f"✅ Uploaded data to gs://{bucket_name}/{destination_blob_name}")

    except Exception as e:
        print(f"❌ Failed to upload, error: {e}")

def load_to_gcp_pipeline():

    raw_data = extract_data_from_url()
    if raw_data:
        df = transform_data(raw_data)
        load_to_gcp(df)
    else:
        logging.info("No data extracted from SpaceX")

if __name__ == "__main__":
    logging.info("Starting the ETL process")
    load_to_gcp_pipeline()
    logging.info("Successfully stored data in GCP")