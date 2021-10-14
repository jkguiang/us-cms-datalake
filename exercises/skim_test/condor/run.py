import argparse
import time
import os.path

from metis.Sample import DBSSample, DirectorySample
from metis.CondorTask import CondorTask
from metis.StatsParser import StatsParser
from metis.Utils import good_sites

from samples import samples_UL as samples

NAME = "DataLakeSkimTests"

cli = argparse.ArgumentParser(description="Submit Data Lake skim test condor jobs")
cli.add_argument(
    "--debug",
    action="store_true", default=False,
    help="Run in debug mode"
)
cli.add_argument(
    "--tag", type=str, required=True,
    help="Unique tag for submissions"
)
cli.add_argument(
    "--xrootd_host", type=str, default="xcache-redirector.t2.ucsd.edu:2042",
    help="<IP>:<port> of desired XRootD host"
)
cli.add_argument(
    "--package", type=str, default="../package.tar.gz",
    help="Skimmer package.tar.gz"
)
cli.add_argument(
    "--sites", type=str, nargs="*", default=["T2_US_UCSD"],
    help="Space-separated list of T2 sites"
)
cli.add_argument(
    "--n_monit_hrs", type=int, default=48,
    help="Number of hours to run Metis for"
)
args = cli.parse_args()

if not os.path.isfile(args.package):
    print("ERROR: {} does not exist!".format(args.package))
    exit()

total_summary = {}
n_updates = args.n_monit_hrs*2 if args.n_monit_hrs > 0 else 1
for _ in range(n_updates): # update every 30 mins
    tasks = []
    if args.debug:
        samples = [samples[0]]
    for sample in samples:
        task = CondorTask(
            sample=sample,
            files_per_output=1,
            output_name="output.root",
            tag=args.tag,
            condor_submit_params={
                "sites": ",".join(args.sites), 
                "classads": [ 
                    ["XRootDHost", args.xrootd_host]
                ]
            },
            cmssw_version="CMSSW_10_6_25",
            scram_arch="slc7_amd64_gcc700",
            input_executable="condor_executable_metis.sh", # your condor executable here
            tarfile=args.package, # your tarfile with assorted goodies here
            special_dir="{0}/{1}".format(NAME, args.tag), # output files into /hadoop/cms/store/<user>/<special_dir>
        )
        tasks.append(task)
    # Set task summary
    for task in tasks:
        task.process()
        total_summary[task.get_sample().get_datasetname()] = task.get_task_summary()

    StatsParser(data=total_summary, webdir="~/public_html/{}_metis".format(NAME.lower())).do()
    time.sleep(30*60)
