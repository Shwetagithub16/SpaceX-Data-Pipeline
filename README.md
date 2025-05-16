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

