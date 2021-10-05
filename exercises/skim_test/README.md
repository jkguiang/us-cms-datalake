### Instructions
1. Create `package.tar.gz`
```
sh create_package.sh
```

(Optional) Test it locally
```
sh run.sh package.tar.gz /path/to/nanoaod.root
```

2. Create configmaps
```
kubectl create configmap skim-test-pkg-configmap --from-file=package.tar.gz
kubectl create configmap skim-test-exe-configmap --from-file=run.sh
```

3. Deploy pod
```
kubectl create -f deploy.yaml
```

4. Ensure Data Lake prototype is set up (cf. parent dir)

5. Start an interactive session on the pod
```
kubectl exec -it skim-test -- /bin/bash
```

6. Run the test
```
sh run.sh package.tar.gz root://redirector.ip:1094//path/to/file.root
```
