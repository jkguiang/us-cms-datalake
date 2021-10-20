import argparse
import time
import os

from metis.Sample import DBSSample, DirectorySample
from metis.CondorTask import CondorTask
from metis.StatsParser import StatsParser
from metis.Utils import good_sites

from samples import samples_UL as samples

NAME = "DataLakeSkimTests"

cli = argparse.ArgumentParser(description="Submit Data Lake skim test condor jobs")
cli.add_argument(
    "--debug",
    action="store_true",
    help="Run in debug mode"
)
cli.add_argument(
    "--python2",
    action="store_true",
    help="Use Python2 to run nanoAOD-tools on the condor worker node"
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

if args.python2:
    CMSSW_VERSION="CMSSW_10_6_25",
    SCRAM_ARCH="slc7_amd64_gcc700",
else:
    CMSSW_VERSION = "CMSSW_12_1_0_pre4_ROOT624"
    SCRAM_ARCH = "slc7_amd64_gcc900"

if not os.path.isfile(args.package):
    print("ERROR: {} does not exist!".format(args.package))
    exit()

# Assemble condor_submit parameters
condor_submit_params = {
    "sites": ",".join(args.sites), 
    "classads": [["XRootDHost", args.xrootd_host]]
}
if args.python2:
    condor_submit_params["classads"].append(["UsePython2", "true"])

token_file = ""
if "BEARER_TOKEN" in os.environ.keys():
    token_file = "/tmp/bt_u{}".format(os.getuid())
    with open(token_file, "w") as f_out:
        f_out.write(os.environ["BEARER_TOKEN"])
elif "BEARER_TOKEN_FILE" in os.environ.keys():
    token_file = os.environ["BEARER_TOKEN_FILE"]
elif "XDG_RUNTIME_DIR" in os.environ.keys():
    token_file = "{0}/bt_u{1}".format(os.environ['XDG_RUNTIME_DIR'], os.getuid())
elif os.path.isfile("/tmp/bt_u{}".format(os.getuid())):
    token_file = "/tmp/bt_u{}".format(os.getuid())

if token_file != "" and os.path.isfile(token_file):
    condor_submit_params["classads"].append(["use_scitokens", "Auto"])
    condor_submit_params["classads"].append(["scitokens_file", token_file])

if args.debug:
    samples = [samples[0]]
    max_jobs = 1
else:
    max_jobs = 0

total_summary = {}
n_updates = args.n_monit_hrs*2 if args.n_monit_hrs > 0 else 1
for _ in range(n_updates): # update every 30 mins
    # Collect tasks
    tasks = []
    for sample in samples:
        task = CondorTask(
            sample=sample,
            files_per_output=1,
            output_name="output.root",
            tag=args.tag,
            condor_submit_params=condor_submit_params,
            cmssw_version=CMSSW_VERSION,
            scram_arch=SCRAM_ARCH,
            input_executable="condor_executable_metis.sh", # your condor executable here
            tarfile=args.package, # your tarfile with assorted goodies here
            special_dir="{0}/{1}".format(NAME, args.tag), # output files into /hadoop/cms/store/<user>/<special_dir>
            max_jobs=max_jobs
        )
        tasks.append(task)
    # Set task summary
    for task in tasks:
        task.process()
        total_summary[task.get_sample().get_datasetname()] = task.get_task_summary()
    # Update monitoring GUI
    StatsParser(data=total_summary, webdir="~/public_html/{}_metis".format(NAME.lower())).do()
    if args.debug:
        break
    # Wait 30 minutes
    time.sleep(30*60)
