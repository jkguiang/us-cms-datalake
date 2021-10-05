#!/bin/bash

usage()
{
    echo "Usage:"
    echo ""
    echo "  sh run.sh PACKAGE.tar.gz NANOAODPATH"
    echo ""
    exit
}

if [ -z $1 ]; then usage; fi
if [ -z $2 ]; then usage; fi

PACKAGE=$(realpath $1)
NANOAODPATH=$2

echo "----------------------------------------------------"
echo "Testing NanoAOD Skimming with the PACKAGE=${PACKAGE}"
echo "on NanoAOD file NANOAODPATH=${NANOAODPATH}"
echo "----------------------------------------------------"
echo ""

# Create a test area to check the package

source /cvmfs/cms.cern.ch/cmsset_default.sh

SCRAMARCH=slc7_amd64_gcc700
# CMSSWVERSION=CMSSW_10_2_13
CMSSWVERSION=CMSSW_10_6_25

# Go to a working directory that will be cleaned afterwards
mkdir -p tmp_test_package
cd tmp_test_package

# Setup environment (If already exists it will leave them be)
export SCRAM_ARCH=${SCRAMARCH} && scramv1 project CMSSW ${CMSSWVERSION}
cd ${CMSSWVERSION}/src/

tar xf ${PACKAGE} # It will overwrite if necessary
cd PhysicsTools/NanoAODTools/
eval `scramv1 runtime -sh`
scram b -j

python scripts/nano_postproc.py \
    ./ \
    ${NANOAODPATH} \
    -b python/postprocessing/examples/keep_and_drop.txt \
    -I PhysicsTools.NanoAODTools.postprocessing.examples.vbsHwwSkimModule \
    vbsHwwSkimModuleConstr

# Copy back the output to parent directory
BASENAMEWITHEXT=$(basename ${NANOAODPATH})
BASENAME=${BASENAMEWITHEXT%.*}
cp ${BASENAME}_Skim.root ../../../../../
