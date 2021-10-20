### Instructions
0. Ensure [ProjectMetis](https://github.com/aminnj/ProjectMetis) is installed and set up (and that the Data Lake prototype is up and running)
1. Create skimmer package (cf. parent dir)
2. Run the Metis submission script
    - Note that Metis needs `tqdm`, so make sure this is installed (should be included in CMSSW 10.6.25)
    - The `debug` flag will run just one job such that you can ensure everything is running properly
```
python run.py --tag=<your tag here> --xrootd_host=<cache:port> --sites T2_US_SITE1 T2_US_SITE2 ...
```
3. Wait...
