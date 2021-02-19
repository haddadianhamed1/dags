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



default_args = {
    'owner': 'airflow',
}
# airflow trigger_dag k8s_print_env --conf '{"parameter":"~/path" }'
param = "{{dag_run.conf.get('parameter')}}"

example_workflow = DAG('k8s_print_env_2',
                         default_args=default_args,
                         schedule_interval=None,
                         start_date=days_ago(2),
                         tags=['k8s_print_environment'])

with example_workflow:
        t1 = KubernetesPodOperator(namespace='airflow-alpaca',
                               image="018025508913.dkr.ecr.us-east-1.amazonaws.com/airflow-alpaca:v0.4.3",
                               cmds=["python",],
                               arguments=["0_print_context.py", param],
                               labels={'runner': 'airflow'},
                               name="airflow-env-pod",
                               image_pull_secrets="regcred",
                               task_id='pod1',
                               is_delete_operator_pod=False,
                               hostnetwork=False,
                               )