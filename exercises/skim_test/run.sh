#!/bin/bash

print_help()
{
    echo "Usage:"
    echo ""
    echo "  sh run.sh [--input_file=/path/to/nanoaod.root] [--package=/path/to/package.tar.gz] [--no_skim] [--debug]"
    echo ""
    exit 0
}

NANOAODPATH=""
PACKAGE=""
SKIM=true
DEBUG=false
PYTHON2=false

# Parse arguments
for arg in "$@"; do
    key=$(echo $arg | cut -f1 -d=)
    val=$(echo $arg | cut -f2 -d=)   
    case "$key" in
        -h) print_help;;
        --input_file) NANOAODPATH=$val;;
        --package) PACKAGE=$(realpath $val);;
        --no_skim) SKIM=false;;
        --debug) DEBUG=true;;
        --python2) PYTHON2=true;;
    esac
done

if [[ "$NANOAODPATH" == "" && "$SKIM" == "true" ]]; then
    echo "ERROR: no input file provided!"
    print_help
fi

if [[ "$SKIM" == "true" ]]; then
    echo "----------------------------------------------------"
    echo "Testing NanoAOD Skimming with the PACKAGE=${PACKAGE}"
    echo "on NanoAOD file NANOAODPATH=${NANOAODPATH}"
    echo "----------------------------------------------------"
    echo ""
else
    echo "----------------------------------------------------"
    echo "Generating NanoAOD Skimming package"
    echo "----------------------------------------------------"
    echo ""
fi

# Go to a working directory that will be cleaned afterwards
ORIG_DIR=$PWD
mkdir -p temp_dir
cd temp_dir

if [[ -f $PACKAGE ]]; then
    tar xf $PACKAGE # It will overwrite if necessary
    cd NanoAODTools
    bash standalone/env_standalone.sh build
    source standalone/env_standalone.sh
else
    git clone https://github.com/jkguiang/nanoAOD-tools.git NanoAODTools
    cd NanoAODTools
    bash standalone/env_standalone.sh build
    source standalone/env_standalone.sh

    # Copy the extra files to where they need to go
    cp ${ORIG_DIR}/extras/* python/postprocessing/examples

    # Get the git information
    git diff > gitdiff.txt
    git status > gitstatus.txt
    git rev-parse HEAD > githash.txt

    # Check if ROOT is on $PATH
    if ! command -v root &> /dev/null; then
        echo "ERROR: ROOT cannot be found and is needed to set up NanoCORE"
        exit 0
    fi

    # Setup NanoCORE
    git clone https://github.com/cmstas/NanoTools
    cd NanoTools/NanoCORE
    make clean
    make -j
    cd ${ORIG_DIR}/temp_dir

    # Tar the PhysicsTools directory
    tar -chJf package.tar.gz NanoAODTools \
        --exclude="NanoAODTools/.git" \
        --exclude="NanoAODTools/data" \
        --exclude="NanoAODTools/python/postprocessing/data" \
        --exclude="NanoAODTools/NanoTools/.git" \
        --exclude="NanoAODTools/package.tar.gz"

    mv package.tar.gz $ORIG_DIR/
    cd NanoAODTools
fi

if [[ "$SKIM" == "true" ]]; then
    if [[ "$PYTHON2" == "true" ]]; then
        python2 scripts/nano_postproc.py \
            ./ \
            ${NANOAODPATH} \
            -b python/postprocessing/examples/keep_and_drop.txt \
            -I PhysicsTools.NanoAODTools.postprocessing.examples.vbsHwwSkimModule \
            vbsHwwSkimModuleConstr
    else
        python3 scripts/nano_postproc.py \
            ./ \
            ${NANOAODPATH} \
            -b python/postprocessing/examples/keep_and_drop.txt \
            -I PhysicsTools.NanoAODTools.postprocessing.examples.vbsHwwSkimModule \
            vbsHwwSkimModuleConstr
    fi

    # Copy back the output to parent directory
    BASENAMEWITHEXT=$(basename ${NANOAODPATH})
    BASENAME=${BASENAMEWITHEXT%.*}
    mv ${BASENAME}_Skim.root $ORIG_DIR/${BASENAME}_skimmed.root
fi

cd $ORIG_DIR
if [[ "$DEBUG" == "false" ]]; then
    # Clean up
    rm -rf temp_dir
fi
