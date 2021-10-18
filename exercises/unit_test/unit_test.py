#!/usr/bin/env python

# BSD 3-Clause License; see https://github.com/scikit-hep/uproot3/blob/master/LICENSE

import argparse
import uproot
import uproot_methods
import numpy
import pandas
import matplotlib.pyplot as pyplot

CA_CHECK = False

class HTTPTokenSource(uproot.HTTPSource):
    """
    A child of HTTPSource that uses the WLCG-approved bearer token discovery algorithm for tokenized requests.
    
    See: https://github.com/WLCG-AuthZ-WG/bearer-token-discovery/blob/master/specification.md
    """

    def __init__(self, path, *args, **kwds):
        kwargs = dict(super().defaults)
        for n in kwargs:
            if n in kwds:
                kwargs[n] = kwds.pop(n)

        super(HTTPTokenSource, self).__init__(path, *args, **kwargs)

    def _read(self, chunkindex):
        import requests, os
        global CA_CHECK
        if not CA_CHECK:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        token = ""
        if "BEARER_TOKEN" in os.environ.keys():
            token = os.environ["BEARER_TOKEN"]
        elif "BEARER_TOKEN_FILE" in os.environ.keys():
            with open(os.eviron["BEARER_TOKEN_FILE"]) as token_file:
                token = token_file.read()
        elif "XDG_RUNTIME_DIR" in os.eviron.keys():
            with open(f"{os.eviron['XDG_RUNTIME_DIR']}/bt_u{os.getuid()}") as token_file:
                token = token_file.read()
        elif os.path.isfile(f"/tmp/bt_u{os.getuid()}"):
            with open(f"/tmp/bt_u{os.getuid()}") as token_file:
                token = token_file.read()
        headers = {}
        if token != "":
            headers["Authorization"] = f"Bearer {token}"
        while True:
            headers["Range"] = "bytes={0}-{1}".format(chunkindex * self._chunkbytes, (chunkindex + 1) * self._chunkbytes - 1)
            response = requests.get(
                self.path,
                headers=headers,
                auth=self.auth,
                verify=CA_CHECK
            )
            if response.status_code == 504:   # timeout, try it again
                pass
            else:
                response.raise_for_status()   # if it's an error, raise exception
                break                         # otherwise, break out of the loop
        data = response.content

        if self._size is None:
            m = self._contentrange.match(response.headers.get("Content-Range", ""))
            if m is not None:
                start_inclusive, stop_inclusive, size = int(m.group(1)), int(m.group(2)), int(m.group(3))
                if size > (stop_inclusive - start_inclusive) + 1:
                    self._size = size
        return numpy.frombuffer(data, dtype=numpy.uint8)

def unit_test(input_file, verbose=False):
    uproot_file = uproot.open(input_file, httpsource=HTTPTokenSource)
    ttree = uproot_file["Events"]
    mu_p4s = uproot_methods.TLorentzVectorArray.from_ptetaphim( 
        *ttree.arrays(["Muon_pt","Muon_eta","Muon_phi","Muon_mass"], outputtype=tuple, entrystop=100000) 
    )
    dimuon_mass = (lambda x:x.i0+x.i1+x.i2+x.i3)(mu_p4s.choose(4)[:,:1]).mass
    pandas.Series(dimuon_mass.flatten()).plot.hist(bins=numpy.linspace(0,200,100), logy=False)
    pyplot.xlabel("$M_{\mu\mu}$", size=14)
    pyplot.ylabel("Events", size=14)
    pyplot.savefig("test.png")
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
