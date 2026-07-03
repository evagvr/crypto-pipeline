from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def start():
    print("Pipeline starting")


def verify_kafka():
    print("Verifying Kafka connection")


def verify_db():
    print("Verifying DB connection")


with DAG(
    dag_id="crypto_pipeline",
    start_date=datetime(2026, 7, 1),
    schedule_interval=timedelta(minutes=5),
    catchup=False,
) as dag:
    start_task = PythonOperator(task_id="start", python_callable=start)
    verify_kafka_task = PythonOperator(
        task_id="verify_kafka", python_callable=verify_kafka
    )
    verify_db_task = PythonOperator(task_id="verify_db", python_callable=verify_db)

    start_task >> verify_kafka_task >> verify_db_task
