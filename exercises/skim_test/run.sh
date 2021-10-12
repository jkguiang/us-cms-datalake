#!/bin/bash

usage()
{
    echo "Usage:"
    echo ""
    echo "  sh run.sh PACKAGE.tar.gz NANOAODPATH [/path/to/package.tar.gz]"
    echo ""
    exit
}

NANOAODPATH=$1

if [ -z $1 ]; then usage; else NANOAODPATH=$1; fi
if [ -z $2 ]; then PACKAGE="package.tar.gz"; else PACKAGE=$(realpath $2); fi

echo "----------------------------------------------------"
echo "Testing NanoAOD Skimming with the PACKAGE=${PACKAGE}"
echo "on NanoAOD file NANOAODPATH=${NANOAODPATH}"
echo "----------------------------------------------------"
echo ""

if [[ -f /opt/cms/cmsset_default.sh ]]; then
    # On a CMSSW container (or pod)
    source /opt/cms/cmsset_default.sh
elif [[ -f /cvmfs/cms.cern.ch/cmsset_default.sh ]]; then
    # On a machine with cvmfs
    source /cvmfs/cms.cern.ch/cmsset_default.sh
else
    echo "ERROR: no known paths to cmsset_default.sh exist!"
    exit
fi

SCRAMARCH=slc7_amd64_gcc700
CMSSWVERSION=CMSSW_10_6_25

# Go to a working directory that will be cleaned afterwards
ORIG_DIR=$PWD
mkdir -p temp_dir
cd temp_dir

# Setup environment (If already exists it will leave them be)
export SCRAM_ARCH=${SCRAMARCH} && scramv1 project CMSSW ${CMSSWVERSION}
cd ${CMSSWVERSION}/src/

if [[ -f $PACKAGE ]]; then
    tar xf $PACKAGE # It will overwrite if necessary
else
    # git clone nanoAOD-tools
    git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
    cd PhysicsTools/NanoAODTools # temp_dir/CMSSW_10_2_13/src/PhysicsTools/NanoAODTools
    git checkout e963c70

    # Copy the extra files to where they need to go
    cp ${ORIG_DIR}/extras/* python/postprocessing/examples

    # Get the git information
    cd $ORIG_DIR
    git diff > temp_dir/${CMSSWVERSION}/src/PhysicsTools/NanoAODTools/gitdiff.txt
    git status > temp_dir/${CMSSWVERSION}/src/PhysicsTools/NanoAODTools/gitstatus.txt
    git rev-parse HEAD > temp_dir/${CMSSWVERSION}/src/PhysicsTools/NanoAODTools/githash.txt

    # Compile with CMSSW
    cd temp_dir/${CMSSWVERSION}/src/PhysicsTools/NanoAODTools/
    cmsenv
    scram b -j

    # Setup NanoCORE
    git clone https://github.com/cmstas/NanoTools
    cd NanoTools/NanoCORE # temp_dir/CMSSW_10_2_13/src/PhysicsTools/NanoAODTools/NanoTools/NanoCORE
    make clean
    make -j
    cd ../../../../ # temp_dir/CMSSW_10_2_13/src/

    # Tar the PhysicsTools directory
    tar -chJf package.tar.gz PhysicsTools \
        --exclude="PhysicsTools/NanoAODTools/.git" \
        --exclude="PhysicsTools/NanoAODTools/data" \
        --exclude="PhysicsTools/NanoAODTools/python/postprocessing/data" \
        --exclude="PhysicsTools/NanoAODTools/NanoTools/.git" \
        --exclude="PhysicsTools/NanoAODTools/package.tar.gz"

    mv package.tar.gz $ORIG_DIR/
fi

cd PhysicsTools/NanoAODTools
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
cp ${BASENAME}_Skim.root $ORIG_DIR/${BASENAME}_skimmed.root

# Clean up
cd $ORIG_DIR
rm -rf temp_dir
