import argparse
import uproot
import uproot_methods
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def unit_test(input_file, verbose=False):
    uproot_file = uproot.open(input_file)
    ttree = uproot_file["Events"]
    mu_p4s = uproot_methods.TLorentzVectorArray.from_ptetaphim( 
        *ttree.arrays(["Muon_pt","Muon_eta","Muon_phi","Muon_mass"],
        outputtype=tuple, entrystop=100000) 
     )
    dimuon_mass = (lambda x:x.i0+x.i1+x.i2+x.i3)(mu_p4s.choose(4)[:,:1]).mass
    pd.Series(dimuon_mass.flatten()).plot.hist(bins=np.linspace(0,200,100), logy=False)
    plt.xlabel("$M_{\mu\mu}$", size=14)
    plt.ylabel("Events", size=14)
    plt.savefig("test.png")
    return

if __name__ == "__main__":
    cli = argparse.ArgumentParser(description="Run US-CMS Data Lake unit test")
    cli.add_argument(
        "-v", "--verbose",
        action="store_true", default=False,
        help="Print verbose output"
    )
    cli.add_argument(
        "--input_file", 
        type=str, default="test.root",
        help="Path to input file on server"
    )
    args = cli.parse_args()
    unit_test(args.input_file, verbose=args.verbose)
