delete:
	- kubectl delete -f deploy.yaml
	- kubectl delete configmap skim-test-exe-configmap
create:
	- kubectl create configmap skim-test-exe-configmap --from-file=run.sh
	- sleep 2
	- kubectl create -f deploy.yaml
