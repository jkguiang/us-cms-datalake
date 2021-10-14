### Instructions
0. Ensure ProjectMetis is installed and setup (and that Data Lake prototype is up and running)
1. Create skimmer package (cf. parent dir)
2. Run the Metis submission script
    - Note that Metis needs `tqdm`, so make sure this is installed (personally, I have this for CMSSW 10.6.25)
```
python run.py --tag <your tag here> --xrootd_host=<cache:port> --sites T2_US_SITE1 T2_US_SITE2 ...
```
3. Wait...
