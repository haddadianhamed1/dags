# dags
https://github.com/airflow-helm/charts/
```
airflow.operators.bash_operator- executes a bash command
airflow.operators.docker_operator- implements Docker operator
airflow.operators.email_operator- sends an email
airflow.operators.hive_operator- executes hql code or hive script in a specific Hive database
airflow.operators.sql_operator- executes sql code in a specific Microsoft SQL database
airflow.operators.slack_operator.SlackAPIOperator- posts messages to a slack channel
airflow.operators.dummy_operator- operator that does literally nothing. It can be used to group tasks in a DAG
```


https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/_modules/airflow/providers/cncf/kubernetes/example_dags/example_kubernetes.html


# call dags externally
```
curl -X POST \
    http://localhost:8080/api/experimental/dags/print_env/dag_runs \
    -H 'Cache-Control: no-cache' \
    -H 'Content-Type: application/json' \
    -d '{"conf":"{\"key\":\"hamed\"}"}'

```
```
airflow trigger_dag print_env --conf '{"key":"hamed" }'
airflow trigger_dag k8s_print_env --conf '{"key":"hamed" }'

airflow trigger_dag k8s_print_env --conf '{"arguments":{"TEST_VAR":"hamed"}}'
airflow trigger_dag k8s_print_env --conf '{"arguments":["hamed"]}'


airflow trigger_dag k8s_print_env --conf '{"parameter":"~/path" }'

```
https://stackoverflow.com/questions/44363243/airflow-pass-parameter-from-cli
