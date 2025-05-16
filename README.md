# 🚀 SpaceX Data Pipeline

This repository contains an **end-to-end data pipeline** built to extract, transform, and load (ETL) SpaceX launch data using modern data engineering tools and best practices. The pipeline is designed to be **production-ready**, **containerized**, and **cloud-deployable** using Google Cloud Platform (GCP).

---

## 📌 Project Overview

This project automates the following ETL workflow:

1. **🔄 Data Ingestion**: Fetches raw SpaceX launch data from the [SpaceX public API](https://api.spacexdata.com/v4/launches).
2. **🧹 Data Cleansing & Validation**: Uses Python to process and validate the raw data.
3. **📦 Data Loading**: Uploads the clean data to **Google Cloud Storage (GCS)** and loads it into **BigQuery**.
4. **🔁 Data Transformation**: Applies further modeling and transformations with **dbt** (Data Build Tool).
5. **🕹️ Orchestration**: Uses **Apache Airflow** to schedule and manage the entire pipeline through DAGs.
6. **☁️ Cloud Deployment**: Entire pipeline is **containerized with Docker**, deployed on **Cloud Run**, and triggered daily via **Cloud Scheduler**.


## 🛠️ Tech Stack

| Layer                | Tools/Tech                            |
|---------------------|----------------------------------------|
| Orchestration       | Apache Airflow                         |
| Data Processing     | Python (Pandas, Requests, etc.)        |
| Data Warehouse      | Google BigQuery                        |
| Data Storage        | Google Cloud Storage                   |
| Transformation      | dbt (BigQuery adapter)                 |
| Containerization    | Docker                                 |
| Deployment          | Cloud Run + Cloud Scheduler            |
| Infrastructure      | Google Cloud Platform (GCP)            |

---

## 🚀 How It Works

### 1. Ingestion
Fetch launch data from the SpaceX API and save it locally or directly upload to GCS.

### 2. Processing
Clean and validate the JSON data. Drop irrelevant fields, fix missing or incorrect values, and prepare it for loading.

### 3. Loading
- Upload raw and clean datasets to GCS.
- Load the clean dataset from GCS into a BigQuery table (`spacex.launch_data`).

### 4. dbt Transformations
Run dbt models to create curated tables and views, including dimension and fact tables for analytics.

### 5. Orchestration with Airflow
Airflow DAG is responsible for:
- Triggering ingestion scripts
- Running dbt transformations
- Managing dependencies and retries

### 6. Cloud Deployment
The Dockerized pipeline is deployed on Cloud Run and invoked daily via Cloud Scheduler.

---

## 🚀 How It Works

### 1. Ingestion
Fetch launch data from the SpaceX API and save it locally or directly upload to GCS.

### 2. Processing
Clean and validate the JSON data. Drop irrelevant fields, fix missing or incorrect values, and prepare it for loading.

### 3. Loading
- Upload raw and clean datasets to GCS.
- Load the clean dataset from GCS into a BigQuery table (`spacex.launch_data`).

### 4. dbt Transformations
Run dbt models to create curated tables and views, including dimension and fact tables for analytics.

### 5. Orchestration with Airflow
Airflow DAG is responsible for:
- Triggering ingestion scripts
- Running dbt transformations
- Managing dependencies and retries

### 6. Cloud Deployment
The Dockerized pipeline is deployed on Cloud Run and invoked daily via Cloud Scheduler.

---

## 🐳 Running Locally with Docker

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/SpaceX-Data-Pipeline.git
   cd SpaceX-Data-Pipeline

2. **Build Docker image:**
   ```bash
   docker build -t spacex-etl .

   

