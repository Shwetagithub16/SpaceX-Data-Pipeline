# Dockerfile

FROM apache/airflow:2.8.1-python3.11

# Install required system and Python packages
USER root
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*


COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/
COPY dbt/ /opt/airflow/dbt/
COPY secrets/ /opt/airflow/secrets/
COPY requirements.txt .
COPY startscript.sh /startscript.sh
RUN chmod +x /startscript.sh
RUN chown -R airflow: /opt/airflow/dbt

# Set up dbt working directory and profiles path
# Copy only the dbt project folder (`my_dbt`) to a clean directory


USER airflow

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/startscript.sh"]
