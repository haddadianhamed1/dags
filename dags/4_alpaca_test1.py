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
def run_this_func(**kwargs):
    print(kwargs['conf'])
    
example_workflow = DAG('alpaca_test_1',
                         default_args=default_args,
                         schedule_interval=None,
                         start_date=days_ago(2),
                         tags=['example'])

with example_workflow:

        start = DummyOperator(task_id='run_this_first')

        t1 = KubernetesPodOperator(namespace='airflow-alpaca',
                               image="018025508913.dkr.ecr.us-east-1.amazonaws.com/airflow-alpaca:v0.4.3",
                               cmds=["python",],
                               arguments=["1_print_account.py"],
                               labels={'runner': 'airflow'},
                               name="airflow-test-pod",
                               image_pull_secrets="regcred",
                               task_id='pod1',
                               is_delete_operator_pod=False,
                               hostnetwork=False,
                               )


        print_conf = PythonOperator(task_id='run_this',
            python_callable=run_this_func,
            provide_context=True,
        )                       
        start >> t1 >> print_conf