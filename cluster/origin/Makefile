delete:
	- kubectl delete -k ./
create:
	#- sed -i '/all.manager/c\all.manager\ $(shell kubectl get pods -l k8s-app=us-cms-datalake-origin-redi -o jsonpath="{.items[0].spec.nodeName}"):2213' xrootd.cfg
	- kubectl apply -k ./
