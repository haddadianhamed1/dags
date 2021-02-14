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

example_workflow = DAG('example_kubernetes_operator',
                         default_args=default_args,
                         schedule_interval=None,
                         start_date=days_ago(2),
                         tags=['example'])

with example_workflow:
        t1 = KubernetesPodOperator(namespace='airflow-alpaca',
                               image="ubuntu:16.04",
                               arguments=["echo", "hello world"],
                               labels={'runner': 'airflow'},
                               name="airflow-test-pod",
                               task_id='pod1',
                               is_delete_operator_pod=False,
                               hostnetwork=False,
                               priority_class_name="medium",
                               )
        t2 = KubernetesPodOperator(namespace='airflow-alpaca',
                                image="ubuntu:16.04",
                                arguments=["echo", "hello world2"],
                                labels={'runner': 'airflow'},
                                name="pod2",
                                task_id='pod2',
                                is_delete_operator_pod=False,
                                hostnetwork=False,
                                )

        t3 = KubernetesPodOperator(namespace='airflow-alpaca',
                                image="ubuntu:16.04",
                                arguments=["echo", "hello world3"],
                                labels={'runner': 'airflow'},
                                name="pod3",
                                task_id='pod3',
                                is_delete_operator_pod=False,
                                hostnetwork=False,
                                )                               

        t4 = KubernetesPodOperator(namespace='airflow-alpaca',
                                image="ubuntu:16.04",
                                arguments=["echo", "hello world4"],
                                labels={'runner': 'airflow'},
                                name="pod4",
                                task_id='pod4',
                                is_delete_operator_pod=False,
                                hostnetwork=False,
                                )
        t1 >> [t2, t3] >> t4
