#for reference to build custom airflow image: https://airflow.apache.org/docs/docker-stack/build.html
FROM apache/airflow:2.3.0

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt .

RUN pip install -r requirements.txt


