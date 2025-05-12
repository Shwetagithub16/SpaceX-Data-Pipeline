This repository contains an end-to-end data pipeline project built to extract, transform, and load (ETL) SpaceX launch data using modern data engineering tools and best practices.
The pipeline is designed to be production-ready, containerized, and cloud-deployable. It orchestrates the flow of raw data ingestion, transformation, validation, and final loading into a data warehouse.

The pipeline automates the following steps:

- Data Ingestion: Pulls raw SpaceX launch data from a public API.

- Data Processing & Cleansing: Transforms and validates the data using Python and great_expectations.

- Data Loading: Stores cleaned data in Google Cloud Storage and loads it into BigQuery.

- Data Transformation: Uses dbt to create semantic models and transformations within BigQuery.

- Orchestration: Apache Airflow orchestrates the entire workflow with a DAG scheduled to run daily.

- Deployment: Entire pipeline is containerized using Docker and deployed to Google Cloud Run, triggered by Cloud Scheduler.
