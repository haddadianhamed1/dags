https://github.com/airflow-helm/charts/tree/main/charts/airflow

helm repo add airflow-stable https://airflow-helm.github.io/charts
helm repo update

# Helm 3
helm install \
  airflow-test \
  airflow-stable/airflow \
  --namespace airflow-v2 \
  --values ./custom-value-simple.yaml
```
1. Get the Airflow Service URL by running these commands:
   export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services airflow-test-web)
   export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
   echo http://$NODE_IP:$NODE_PORT/

2. Open Airflow in your web browser
```

```
kubectl port-forward airflow-test-web-6db86b4f9c-mz4zg -n airflow-v2 8080:8080

```

```
helm upgrade \
  airflow-test \
  airflow-stable/airflow \
  --namespace airflow-v2 \
  --values ./custom-value-simple.yaml
```


# k8s
```
# Helm 3
helm install \
  airflow-k8s \
  airflow-stable/airflow \
  --namespace airflow-k8s \
  --values ./custom-value-kubernetes.yaml

helm upgrade \
  airflow-k8s \
  airflow-stable/airflow \
  --namespace airflow-k8s \
  --values ./custom-value-kubernetes.yaml  
```


# k8s git
```
helm install \
  airflow-k8s \
  airflow-stable/airflow \
  --namespace airflow-alpaca \
  --values ./airflow-value-final.yaml


helm upgrade \
  airflow-k8s \
  airflow-stable/airflow \
  --namespace airflow-alpaca \
  --values ./airflow-value-final.yaml

kubectl port-forward airflow-k8s-web-c7ffdbc4f-qjx5b -n airflow-alpaca 8080:8080
```