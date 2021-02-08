import datetime
import logging
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

hello_dag = DAG(
        "lesson1.excercise1",
        start_date=datetime.datetime.now(),
        schedule_interval='@daily')

hello_task = PythonOperator(
        task_id="hello_world_task",
        python_callable=hello_world,
        dag=hello_dag)

def hello_world():
    logging.info("Hello World")