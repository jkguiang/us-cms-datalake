delete:
	- kubectl delete -k ./
create:
	#- sed -i '/pss.origin/c\pss.origin\ $(shell kubectl get pods -l k8s-app=us-cms-datalake-origin-redi -o jsonpath="{.items[0].spec.nodeName}"):2094' xrootd.cfg
	- kubectl apply -k ./
