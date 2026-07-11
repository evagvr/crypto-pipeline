from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def start():
    print("Pipeline starting")


def verify_kafka():
    from kafka import KafkaProducer

    try:
        producer = KafkaProducer(bootstrap_servers="kafka:9092")
        producer.close()
        print("Kafka connection succesful")
    except Exception as e:
        raise Exception(f"Kafka connection failed: {e}")


def verify_db():
    import os
    from sqlalchemy import create_engine, text

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    connection_string = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
    engine = create_engine(connection_string)
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as e:
        raise Exception(f"Database connection failed: {e}")


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
