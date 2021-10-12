### Instructions
1. Grab a few test files and copy them to the Data Lake origins
  - File 1: `/store/mc/RunIIFall17NanoAODv7/GluGluHToZZTo4L_M130_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/100000/F6DB020F-DE57-B544-BB67-CDE6016BB401.root`
  - File 2: `/store/mc/RunIIFall17NanoAODv7/GluGluHToZZTo4L_M130_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/100000/3DC6D034-831F-9F49-9456-94544538CCB8.root`
  - File 3: `/store/mc/RunIIFall17NanoAODv7/GluGluHToZZTo4L_M130_13TeV_powheg2_JHUGenV7011_pythia8/NANOAODSIM/PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/100000/5C84FDB1-E59C-6E4E-B74A-F6337E486123.root`

(Optional) You can also run the test 'locally' by using the included python file:
```
python unit_test.py --input_file=root://cache.redi:port//path/to/file
```
If you choose to do this, be sure that you have the following packages installed: `uproot3`, `numpy`, `matplotlib`, `pandas`

2. Create configmap for executable
```
kubectl create configmap datalake-test-exe-configmap --from-file=run.sh
```

3. Deploy pod
```
kubectl create -f deploy.yaml
```
