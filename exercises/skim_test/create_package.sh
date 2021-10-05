#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh

SCRAMARCH=slc7_amd64_gcc700
# CMSSWVERSION=CMSSW_10_2_13
CMSSWVERSION=CMSSW_10_6_25

# Go to a working directory that will be cleaned afterwards
rm -rf tmp_create_package
mkdir -p tmp_create_package
cd tmp_create_package

# Setup environment
export SCRAM_ARCH=${SCRAMARCH} && scramv1 project CMSSW ${CMSSWVERSION}
cd ${CMSSWVERSION}/src/ # tmp_create_package/CMSSW_10_2_13/src/

# git clone the nanoAOD-tools
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
cd PhysicsTools/NanoAODTools # tmp_create_package/CMSSW_10_2_13/src/PhysicsTools/NanoAODTools
git checkout e963c70

# Copy the extra files
cp ../../../../../extra/* python/postprocessing/examples

# Get the git information
cd ../../../../../
git diff > tmp_create_package/${CMSSWVERSION}/src/PhysicsTools/NanoAODTools/gitdiff.txt
git status > tmp_create_package/${CMSSWVERSION}/src/PhysicsTools/NanoAODTools/gitstatus.txt
git rev-parse HEAD > tmp_create_package/${CMSSWVERSION}/src/PhysicsTools/NanoAODTools/githash.txt
cd tmp_create_package/${CMSSWVERSION}/src/PhysicsTools/NanoAODTools/

# Setup and compile
cmsenv
scram b -j

# Copy NanoCORE
cp -r ../../../../../NanoTools .
cd NanoTools/NanoCORE # tmp_create_package/CMSSW_10_2_13/src/PhysicsTools/NanoAODTools/NanoTools/NanoCORE

# Re-compile NanoCORE to make sure
make clean
make -j

cd ../../../../ # tmp_create_package/CMSSW_10_2_13/src/

# Tar the PhysicsTools directory
tar -chJf package.tar.gz PhysicsTools \
    --exclude="PhysicsTools/NanoAODTools/.git" \
    --exclude="PhysicsTools/NanoAODTools/data" \
    --exclude="PhysicsTools/NanoAODTools/python/postprocessing/data" \
    --exclude="PhysicsTools/NanoAODTools/NanoTools/.git" \
    --exclude="PhysicsTools/NanoAODTools/package.tar.gz"

# Copy the package back down to parent directory
mv package.tar.gz ../../../

# Go back down to parent directory and clean up the tmp_create_package
cd ../../../ # back to where I started
rm -rf tmp_create_package
