from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'kubernetes_hamed', 
    default_args=default_args, 
    schedule_interval=timedelta(days = 1))


dummy_task_1 = DummyOperator(task_id='start', dag=dag)

hello_task_2 = KubernetesPodOperator(namespace='hamed-final',
                          image="python:3.6",
                          cmds=["python","-c"],
                          arguments=["print('hello, hi hi hi hi world')"],
                          labels={"foo": "bar"},
                          name="hello-task",
                          task_id="hello-task",
                          get_logs=True,
                          dag=dag
                          )

testing_3 = KubernetesPodOperator(namespace='hamed-final',
                          image="ubuntu:16.04",
                          cmds=["python","-c"],
                          arguments=["print('hello world')"],
                          labels={"foo": "bar"},
                          name="fail",
                          task_id="testing-task",
                          get_logs=True,
                          dag=dag
                          )

end = DummyOperator(task_id='end', dag=dag)


dummy_task_1 >> hello_task_2 >> testing_3