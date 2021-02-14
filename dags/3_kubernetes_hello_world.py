from datetime import datetime as dt
from datetime import timedelta
from airflow.utils.dates import days_ago
#The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
#importing the operators required
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

#these args will get passed to each operator
#these can be overridden on a per-task basis during operator #initialization
#notice the start_date is any date in the past to be able to run it #as soon as it's created
default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='example_kubernetes_operator',
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['example'],
) as dag:
    k = KubernetesPodOperator(
        namespace='default',
        image="ubuntu:16.04",
        cmds=["bash", "-cx"],
        arguments=["echo", "10"],
        labels={"foo": "bar"},
        secrets=[secret_file, secret_env, secret_all_keys],
        ports=[port],
        volumes=[volume],
        volume_mounts=[volume_mount],
        env_from=configmaps,
        name="airflow-test-pod",
        task_id="task",
        affinity=affinity,
        is_delete_operator_pod=True,
        hostnetwork=False,
        tolerations=tolerations,
        init_containers=[init_container],
        priority_class_name="medium",
    )