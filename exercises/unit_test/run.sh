#!/bin/bash

print_help() {
    echo "usage: ./run.sh --input_file=root://URL:PORT//path/to/file.root"
    echo ""
    echo "Run US-CMS Data Lake unit test"
    echo ""
    echo "required arguments:"
    echo "  --input_file root://URL:PORT//path/to/file.root   location of test ROOT file"
    echo ""
    echo "optional arguments:"
    echo "  -h                       display this message"
}

input_file=""

# Parse arguments
for arg in "$@"; do
    key=$(echo $arg | cut -f1 -d=)
    val=$(echo $arg | cut -f2 -d=)   
    case "$key" in
        -h) print_help; exit 0;;
        --input_file) input_file=${val};;
    esac
done

# Set up
tar -zxvf package.tar.gz
source /root/miniconda3/etc/profile.d/conda.sh
conda activate test-env

# Write test script
cat > test.py << EOL
import uproot
import uproot_methods
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
uproot_file = uproot.open("${input_file}")
ttree = uproot_file["Events"]
mu_p4s = uproot_methods.TLorentzVectorArray.from_ptetaphim( 
    *ttree.arrays(["Muon_pt","Muon_eta","Muon_phi","Muon_mass"],
    outputtype=tuple, entrystop=100000) 
 )
dimuon_mass = (lambda x:x.i0+x.i1+x.i2+x.i3)(mu_p4s.choose(4)[:,:1]).mass
pd.Series(dimuon_mass.flatten()).plot.hist(bins=np.linspace(0,200,100), logy=False)
plt.xlabel("\$M_{\\mu\\mu}$", size=14)
plt.ylabel("Events", size=14)
plt.savefig("test.png")
EOL

# Run test script
if [[ "${input_file}" != "" ]]; then
    python test.py
else
    echo "ERROR: no input file provided!"
    echo ""
    print_help
fi
