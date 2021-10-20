### Instructions
0. Ensure Data Lake prototype is set up (cf. parent dir)

1. Create the skimmer package
    - Ensure that you have ROOT available (e.g. in a CMSSW env), since it is needed to compile NanoCORE
```
sh run.sh --no_skim
```
(Optional) Run the skimmer locally
```
sh run.sh --input_file=root://cache:2094//path/to/file.root --package=/path/to/package.tar.gz
```

2. Make a copy of it somewhere that is publicly accessible
```
cp package.tar.gz ~/public_html/dump/package.tar.gz
chmod 755 ~/public_html/dump/package.tar.gz
```

3. Create configmap for executable
```
kubectl create configmap skim-test-exe-configmap --from-file=run.sh
```

4. Deploy pod (and potentially wait > 40 minutes)
```
kubectl create -f deploy.yaml
```

5. Start an interactive session on the pod
```
kubectl exec -it skim-test-<hash> -- /bin/bash
```

6. Download the skimmer package
```
curl -O http://uaf-10.t2.ucsd.edu/~username/dump/package.tar.gz
```

7. Run the test
```
sh run.sh --input_file=root://cache:2094//path/to/file.root --package=/path/to/package.tar.gz
```
