delete:
	- kubectl delete -f deploy.yaml
	- kubectl delete configmap us-cms-datalake-test-exe-configmap
create:
	- kubectl create configmap us-cms-datalake-test-exe-configmap --from-file=run.sh
	- sleep 2
	- kubectl create -f deploy.yaml
