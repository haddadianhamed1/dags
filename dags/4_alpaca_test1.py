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

#these args will get passed to each operator
#these can be overridden on a per-task basis during operator #initialization
#notice the start_date is any date in the past to be able to run it #as soon as it's created
default_args = {
    'owner': 'airflow',
}

example_workflow = DAG('alpaca_test_1',
                         default_args=default_args,
                         schedule_interval=None,
                         start_date=days_ago(2),
                         tags=['example'])

with example_workflow:

        start = DummyOperator(task_id='run_this_first')

        t1 = KubernetesPodOperator(namespace='airflow-alpaca',
                               image="hhaddadian/alpaca:v0.1.0",
                               arguments=["python -c 'import app;app.print_account()'"],
                               labels={'runner': 'airflow'},
                               name="airflow-test-pod",
                               image_pull_secrets="regcred",
                               task_id='pod1',
                               is_delete_operator_pod=False,
                               hostnetwork=False,
                               priority_class_name="medium",
                               )
        start >> t1 