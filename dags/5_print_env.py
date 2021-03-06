from datetime import datetime as dt
from datetime import timedelta
from airflow.utils.dates import days_ago
#The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
#importing the operators required
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from kubernetes.client import models as k8s

import os

default_args = {
    'owner': 'airflow',
}
def run_this_func(**context):
    print("context", context)
    print("Remotely received value of {} for key=message".format(context["dag_run"].conf["key"]))


example_workflow = DAG('print_env',
                         default_args=default_args,
                         schedule_interval=None,
                         start_date=days_ago(2),
                         tags=['print_environment'])

with example_workflow:

        print_conf = PythonOperator(task_id='run_this',
            python_callable=run_this_func,
            provide_context=True,
        )         
        print_conf2 = PythonOperator(task_id='run_this2',
            python_callable=run_this_func,
            provide_context=True,
        )            

        print_conf >> print_conf2