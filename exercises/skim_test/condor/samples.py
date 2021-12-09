#!/bin/env python

from metis.Sample import FilelistSample, DBSSample, DirectorySample
from metis.File import EventsFile

# Specify a dataset name and a short name for the output root file on nfs
samples_v7 = [

        # 2016 NanoAODv7
        DBSSample(dataset="/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM"),
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM"),
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"), # 67860400
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"), # 107604800
        DBSSample(dataset="/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v2/NANOAODSIM"),
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),

        # 2017 NanoAODv7
        # DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 33073306
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 44627200
        # DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 30008250
        # DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 39521230
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 39536839
        # DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 316134
        # DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017RECOSIMstep_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 47990369
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017RECOSIMstep_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 49011552
        DBSSample(dataset="/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 28380110
        DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 61761347
        DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 56648453
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 68812194
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 197613000
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 43506449
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 4925829
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 7932650
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 245978
        DBSSample(dataset="/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 9332943
        # DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 5499293
        DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 7216085
        DBSSample(dataset="/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 149000
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 10987679
        # DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 16075000
        # DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 97920639
        # DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext2-v1/NANOAODSIM"), # 86706666
        DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 6964071
        # DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 965198
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext3-v1/NANOAODSIM"), # 988000
        DBSSample(dataset="/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 986000
        DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 13276146
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 1000000
        DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 240000
        # DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 232300
        DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 962000
        # DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 1000000
        DBSSample(dataset="/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 9994191
        # DBSSample(dataset="/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 8782525
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1/NANOAODSIM"), # 6127285
        # DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 5635539
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 4955102
        DBSSample(dataset="/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 3675910
        DBSSample(dataset="/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 5982064
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 9883805
        DBSSample(dataset="/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM"), # 2000000

        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 71026861
        # DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 39392062
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 46976952
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 100194597
        DBSSample(dataset="/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 28701360
        DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 57137426
        DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 59929205
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 64310000
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 100790000
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext3-v1/NANOAODSIM"), # 199829998
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 4911941
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 13280000
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 9632600
        DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 7525991
        DBSSample(dataset="/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 150000
        # DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 10749269
        DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 11248318
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 6689900
        # DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM"), # 98870000
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 958000
        DBSSample(dataset="/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 248600
        DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 13736000
        DBSSample(dataset="/WZG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 1960000
        DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 240000
        DBSSample(dataset="/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 250000
        DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 250000
        # DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 185000
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM"), # 800000
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        # DBSSample(dataset="/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 2321506
        DBSSample(dataset="/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM"), # 9592768
        DBSSample(dataset="/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 19199100
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT1_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 5823328
        # DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 1086487
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT1_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 7636887
        # DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 1085847
        DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 79090800
        DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 154307600
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 19890000
        DBSSample(dataset="/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1/NANOAODSIM"), # 7758900

        # Data 2016 (NanoAODv7)
        DBSSample(dataset="/DoubleEG/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020-v2/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020_17Jul2018-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016H-02Apr2020-v1/NANOAOD"), #

        # Data 2017 (NanoAODv7)
        DBSSample(dataset="/DoubleEG/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2017F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2017F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2017F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2017F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2017F-02Apr2020-v1/NANOAOD"), #

        # Data 2018 (NanoAODv7)
        DBSSample(dataset="/DoubleMuon/Run2018A-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020_17Jul2018-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018A-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018A-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018A-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018B-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018D-02Apr2020-v1/NANOAOD"), #

        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_6_20210313_RunIIAutumn18NanoAOD_v2/merged",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_6_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
            ),
        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_m2_RunIIAutumn18NanoAOD_VBSWWH_C2V_m2_v3/merged",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_m2_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
            ),
        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_3_20210314_RunIIAutumn18NanoAOD_VBSWWH_C2V_3_v3/merged",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_3_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
            ),
        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3/merged",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_4p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
            ),
        DirectorySample(
            location = "/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3_ext1/merged/",
            dataset = "/VBSWmpWmpHToLNuLNu_C2V_4p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1_ext1/NANOAODSIM",
            ),

        ]

samples_UL = [

        # 2018 Data
        DBSSample(dataset="/DoubleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018B-UL2018_MiniAODv1_NanoAODv2-v2/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/EGamma/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        # DBSSample(dataset="/SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v2/NANOAOD"), #

        # Data 2017 (NanoAODv7)
        DBSSample(dataset="/DoubleEG/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 54.04  , nfiles: 43  , nevents: 58088760  , nlumis: 26447
        DBSSample(dataset="/DoubleEG/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 61.81  , nfiles: 56  , nevents: 65181125  , nlumis: 59165
        DBSSample(dataset="/DoubleEG/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 24.69  , nfiles: 28  , nevents: 25911432  , nlumis: 27927
        DBSSample(dataset="/DoubleEG/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 57.43  , nfiles: 53  , nevents: 56241190  , nlumis: 45495
        DBSSample(dataset="/DoubleEG/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")       , #     filesizeGB: 77.78  , nfiles: 66  , nevents: 74344288  , nlumis: 60474
        DBSSample(dataset="/DoubleMuon/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 12.83  , nfiles: 15  , nevents: 14501767  , nlumis: 26734
        DBSSample(dataset="/DoubleMuon/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 46.53  , nfiles: 36  , nevents: 49636525  , nlumis: 57320
        DBSSample(dataset="/DoubleMuon/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 21.75  , nfiles: 23  , nevents: 23075733  , nlumis: 28105
        DBSSample(dataset="/DoubleMuon/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 52.02  , nfiles: 41  , nevents: 51589661  , nlumis: 44980
        DBSSample(dataset="/DoubleMuon/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 79.59  , nfiles: 55  , nevents: 79756560  , nlumis: 60685
        DBSSample(dataset="/MuonEG/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 4.81   , nfiles: 8   , nevents: 4453465   , nlumis: 26734
        DBSSample(dataset="/MuonEG/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 17.69  , nfiles: 21  , nevents: 15595214  , nlumis: 57320
        DBSSample(dataset="/MuonEG/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 10.34  , nfiles: 13  , nevents: 9164365   , nlumis: 28105
        DBSSample(dataset="/MuonEG/Run2017E-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 22.55  , nfiles: 20  , nevents: 19043421  , nlumis: 44980
        DBSSample(dataset="/MuonEG/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")         , #     filesizeGB: 31.04  , nfiles: 33  , nevents: 25776363  , nlumis: 60631
        DBSSample(dataset="/SingleElectron/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD") , #     filesizeGB: 49.17  , nfiles: 53  , nevents: 60537490  , nlumis: 26448
        DBSSample(dataset="/SingleElectron/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD") , #     filesizeGB: 119.06 , nfiles: 96  , nevents: 136637888 , nlumis: 59164
        DBSSample(dataset="/SingleElectron/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD") , #     filesizeGB: 44.23  , nfiles: 38  , nevents: 51526710  , nlumis: 27927
        DBSSample(dataset="/SingleElectron/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD") , #     filesizeGB: 94.05  , nfiles: 85  , nevents: 102117532 , nlumis: 45490
        DBSSample(dataset="/SingleElectron/Run2017F-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD") , #     filesizeGB: 120.92 , nfiles: 117 , nevents: 126793514 , nlumis: 59668
        DBSSample(dataset="/SingleMuon/Run2017B-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 102.64 , nfiles: 110 , nevents: 136300266 , nlumis: 26734
        DBSSample(dataset="/SingleMuon/Run2017C-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 130.59 , nfiles: 139 , nevents: 165652756 , nlumis: 57320
        DBSSample(dataset="/SingleMuon/Run2017D-UL2017_MiniAODv1_NanoAODv2-v1/NANOAOD")     , #     filesizeGB: 55.42  , nfiles: 58  , nevents: 70361660  , nlumis: 28105
        DBSSample(dataset="/SingleMuon/Run2017E-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD")     , #     filesizeGB: 131.35 , nfiles: 135 , nevents: 154626280 , nlumis: 44971
        DBSSample(dataset="/SingleMuon/Run2017F-UL2017_MiniAODv1_NanoAODv2-v2/NANOAOD")     , #     filesizeGB: 211.48 , nfiles: 174 , nevents: 242140980 , nlumis: 60685

        # Data 2016 (NanoAODv7)
        DBSSample(dataset="/DoubleEG/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleEG/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/DoubleMuon/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020-v2/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016E-02Apr2020_17Jul2018-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/MuonEG/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleElectron/Run2016H-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016B-02Apr2020_ver1-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016B-02Apr2020_ver2-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016C-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016D-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016E-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016F-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016G-02Apr2020-v1/NANOAOD"), #
        DBSSample(dataset="/SingleMuon/Run2016H-02Apr2020-v1/NANOAOD"), #

        # 2018 MC
        # Top backgrounds
        # # ttbar
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                  , # filesizeGB :  1055.12 , nfiles :  465 , nevents :  486770000 , nlumis :  486770
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                         , # filesizeGB :  313.34  , nfiles :  181 , nevents :  148470000 , nlumis :  148470
        # single top                                                                                                                                                                                                                                       
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")            , # filesizeGB :  23.47   , nfiles :  10  , nevents :  11695231  , nlumis :  11328
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                , # filesizeGB :  23.11   , nfiles :  10  , nevents :  11518444  , nlumis :  111656
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                    , # filesizeGB :  32.34   , nfiles :  69  , nevents :  19957999  , nlumis :  19958
        DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")   , # filesizeGB :  40.01   , nfiles :  30  , nevents :  23421300  , nlumis :  234213
        DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")       , # filesizeGB :  81.19   , nfiles :  37  , nevents :  47707100  , nlumis :  477071
        # ttW                                                                                                                                                                                                                                              
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                        , # filesizeGB :  28.45   , nfiles :  12  , nevents :  10522657  , nlumis :  9995
        # ttZ                                                                                                                                                                                                                                              
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                , # filesizeGB :  51.28   , nfiles :  18  , nevents :  19992000  , nlumis :  19992
        # Boson backgrounds                                                                                                                                                                                                                                
        # DY                                                                                                                                                                                                                                               
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                          , # filesizeGB :  84.93   , nfiles :  46  , nevents :  99449093  , nlumis :  99427
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                              , # filesizeGB :  120.19  , nfiles :  53  , nevents :  98433266  , nlumis :  93924
        # W                                                                                                                                                                                                                                                
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                   , # filesizeGB :  85.55   , nfiles :  45  , nevents :  83009353  , nlumis :  75385
        # ssWW                                                                                                                                                                                                                                             
        DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                            , # filesizeGB :  2.09    , nfiles :  19  , nevents :  998000    , nlumis :  998
        # WW                                                                                                                                                                                                                                               
        DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                                       , # filesizeGB :  19.17   , nfiles :  21  , nevents :  15670000  , nlumis :  15670
        # WZ                                                                                                                                                                                                                                               
        DBSSample(dataset="/WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                         , # filesizeGB :  128.13  , nfiles :  54  , nevents :  89670000  , nlumis :  89670
        # ZZ                                                                                                                                                                                                                                               
        DBSSample(dataset="/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                            , # filesizeGB :  138.39  , nfiles :  65  , nevents :  99218000  , nlumis :  99218
        # Higgs samples                                                                                                                                                                                                                                    
        DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                  , # filesizeGB :  29.33   , nfiles :  16  , nevents :  10002677  , nlumis :  9257
        DBSSample(dataset="/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                     , # filesizeGB :  29.23   , nfiles :  11  , nevents :  9909517   , nlumis :  9391
        # Rare multi-X backgrounds                                                                                                                                                                                                                         
        DBSSample(dataset="/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                        , # filesizeGB :  8       , nfiles :  21  , nevents :  2984000   , nlumis :  2984
        DBSSample(dataset="/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                        , # filesizeGB :  7.2     , nfiles :  21  , nevents :  2690000   , nlumis :  2690
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                            , # filesizeGB :  3.04    , nfiles :  19  , nevents :  1000000   , nlumis :  1000
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")                                            , # filesizeGB :  1.47    , nfiles :  4   , nevents :  500000    , nlumis :  500

        # Not used yet
        # DBSSample(dataset="/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        # DBSSample(dataset="/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        # DBSSample(dataset="/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM"), # 200000
        # DBSSample(dataset="/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1/NANOAODSIM"), # 9592768

        # 2017 MC
        # Top backgrounds
        # # ttbar
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                , # filesizeGB : 790.81 , nfiles : 305 , nevents : 355826000 , nlumis : 355826
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                       , # filesizeGB : 231.16 , nfiles : 85  , nevents : 106978000 , nlumis : 106978
        # single top
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")          , # filesizeGB : 16.96  , nfiles : 16  , nevents : 8238224   , nlumis : 7982
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")              , # filesizeGB : 17.47  , nfiles : 9   , nevents : 8498506   , nlumis : 8233
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                  , # filesizeGB : 23.52  , nfiles : 51  , nevents : 14162000  , nlumis : 14162
        DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM") , # filesizeGB : 42.45  , nfiles : 20  , nevents : 24265600  , nlumis : 242656
        DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")     , # filesizeGB : 79.87  , nfiles : 62  , nevents : 45754100  , nlumis : 457541
        # ttW
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                      , # filesizeGB : 20.58  , nfiles : 9   , nevents : 7464889   , nlumis : 7089
        # ttZ
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                              , # filesizeGB : 37.16  , nfiles : 14  , nevents : 14196000  , nlumis : 14196
        # Boson backgrounds
        # DY
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                        , # filesizeGB : 59.79  , nfiles : 31  , nevents : 68072143  , nlumis : 68472
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                            , # filesizeGB : 128.43 , nfiles : 72  , nevents : 102486448 , nlumis : 976795
        # W
        DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                 , # filesizeGB : 86.02  , nfiles : 42  , nevents : 81254459  , nlumis : 73794
        # ssWW
        DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                          , # filesizeGB : 2.09   , nfiles : 1   , nevents : 1000000   , nlumis : 10000
        # WW
        DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                                     , # filesizeGB : 20.08  , nfiles : 30  , nevents : 15883000  , nlumis : 15883
        # WZ
        DBSSample(dataset="/WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                       , # filesizeGB : 92.27  , nfiles : 50  , nevents : 62930000  , nlumis : 62930
        # ZZ
        DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                                     , # filesizeGB : 3.44   , nfiles : 3   , nevents : 2708000   , nlumis : 2708
        # Higgs samples
        DBSSample(dataset="/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                , # filesizeGB : 29.3   , nfiles : 31  , nevents : 9804430   , nlumis : 9074
        DBSSample(dataset="/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                   , # filesizeGB : 29.68  , nfiles : 13  , nevents : 9897140   , nlumis : 9379
        # Rare multi-X backgrounds
        DBSSample(dataset="/TWZToLL_thad_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                      , # filesizeGB : 5.69   , nfiles : 6   , nevents : 2090000   , nlumis : 2090
        DBSSample(dataset="/TWZToLL_tlept_Whad_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                      , # filesizeGB : 5.69   , nfiles : 32  , nevents : 2066000   , nlumis : 2066
        DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                          , # filesizeGB : 2.15   , nfiles : 10  , nevents : 701000    , nlumis : 701
        DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM")                                          , # filesizeGB : 1.08   , nfiles : 5   , nevents : 358000    , nlumis : 358

        # 2016 NanoAODv7
        DBSSample(dataset="/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM"),
        DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1/NANOAODSIM"),
        DBSSample(dataset="/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"), # 67860400
        DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"), # 107604800
        DBSSample(dataset="/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv7-Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tWll_5f_LO_13TeV-MadGraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v2/NANOAODSIM"),
        DBSSample(dataset="/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),
        DBSSample(dataset="/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/NANOAODSIM"),

        # Signal samples

        # DirectorySample(location="/hadoop/cms/store/user/jguiang/VBSWWHSignalGeneration/VBSWWH_Incl_C2V4p5_privateMC_102x_NANOAODSIM_v1.1.0/merged/", dataset="/VBSWmpWmpH_C2V_4p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer16NanoAODv7/NANOAODSIM")  , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL16APVNanoAODv2_v1_NANOAODSIM_v1", dataset="/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL16APVNanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL16NanoAODv2_v1_NANOAODSIM_v1", dataset="/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL16NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL17NanoAODv2_v1-ext1_NANOAODSIM_v1", dataset="/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL17NanoAODv2_v1-ext1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL17NanoAODv2_v1_NANOAODSIM_v1", dataset="/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL17NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL18NanoAODv2_v1-ext1_NANOAODSIM_v1", dataset="/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL18NanoAODv2_v1-ext1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL18NanoAODv2_v1_NANOAODSIM_v1", dataset="/VBSWWHToLNuLNubb_C2V_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL18NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1

        DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_CV_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL16APVNanoAODv2_v1_NANOAODSIM_v1/merged/", dataset="/VBSWWHToLNuLNubb_CV_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL16APVNanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_CV_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL16NanoAODv2_v1_NANOAODSIM_v1/merged/", dataset="/VBSWWHToLNuLNubb_CV_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL16NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_CV_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL17NanoAODv2_v1_NANOAODSIM_v1/merged/", dataset="/VBSWWHToLNuLNubb_CV_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL17NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_CV_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL18NanoAODv2_v1_NANOAODSIM_v1/merged/", dataset="/VBSWWHToLNuLNubb_CV_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL18NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1

        DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C3_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL16APVNanoAODv2_v1_NANOAODSIM_v1/merged/", dataset="/VBSWWHToLNuLNubb_C3_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL16APVNanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C3_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL16NanoAODv2_v1_NANOAODSIM_v1/merged/", dataset="/VBSWWHToLNuLNubb_C3_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL16NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C3_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL17NanoAODv2_v1_NANOAODSIM_v1/merged/", dataset="/VBSWWHToLNuLNubb_C3_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL17NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/VBSWWHToLNuLNubb_C3_TuneCP5_madgraph_pythia8_PRIVATE_RunIISummer20UL18NanoAODv2_v1_NANOAODSIM_v1/merged/", dataset="/VBSWWHToLNuLNubb_C3_TuneCP5_madgraph_pythia8/PRIVATE_RunIISummer20UL18NanoAODv2_v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1

        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL17_VBSWWH_incl_v2_C2V_m2p5_Azure_v2/merged/" , dataset="/VBSWmpWmpH_C2V_m2p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL17NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL17_VBSWWH_incl_v2_C2V_m2_Azure_v2/merged/"   , dataset="/VBSWmpWmpH_C2V_m2_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL17NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")   , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL17_VBSWWH_incl_v2_C2V_m1_Azure_v2/merged/"   , dataset="/VBSWmpWmpH_C2V_m1_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL17NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")   , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL17_VBSWWH_incl_v2_C2V_0_Azure_v2/merged/"    , dataset="/VBSWmpWmpH_C2V_0_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL17NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")    , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL17_VBSWWH_incl_v2_C2V_1_Azure_v2/merged/"    , dataset="/VBSWmpWmpH_C2V_1_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL17NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")    , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL17_VBSWWH_incl_v2_C2V_3_Azure_v2/merged/"    , dataset="/VBSWmpWmpH_C2V_3_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL17NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")    , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL17_VBSWWH_incl_v2_C2V_4_Azure_v2/merged/"    , dataset="/VBSWmpWmpH_C2V_4_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL17NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")    , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL17_VBSWWH_incl_v2_C2V_4p5_Azure_v2/merged/"  , dataset="/VBSWmpWmpH_C2V_4p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL17NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")  , # filesizeGB : 4.6 , nfiles : 14 , nevents : 349750 , nlumis : -1

        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL18_VBSWWH_incl_v2_C2V_m2p5_Azure/merged/"    , dataset="/VBSWmpWmpH_C2V_m2p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM") , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL18_VBSWWH_incl_v2_C2V_m2_Azure/merged/"      , dataset="/VBSWmpWmpH_C2V_m2_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")   , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL18_VBSWWH_incl_v2_C2V_m1_Azure/merged/"      , dataset="/VBSWmpWmpH_C2V_m1_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")   , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL18_VBSWWH_incl_v2_C2V_0_Azure/merged/"       , dataset="/VBSWmpWmpH_C2V_0_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")    , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL18_VBSWWH_incl_v2_C2V_1_Azure/merged/"       , dataset="/VBSWmpWmpH_C2V_1_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")    , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL18_VBSWWH_incl_v2_C2V_3_Azure/merged/"       , dataset="/VBSWmpWmpH_C2V_3_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")    , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL18_VBSWWH_incl_v2_C2V_4_Azure/merged/"       , dataset="/VBSWmpWmpH_C2V_4_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")    , # filesizeGB : x.x , nfiles : xx , nevents : xxxxxx , nlumis : -1
        # DirectorySample(location="/hadoop/cms/store/user/phchang/VBSHWWSignalGeneration/RunIISummer20UL18_VBSWWH_incl_v2_C2V_4p5_Azure/merged/"     , dataset="/VBSWmpWmpH_C2V_4p5_TuneCP5_13TeV-madgraph-pythia8/PRIVATE_RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM")  , # filesizeGB : 8.4 , nfiles : 26 , nevents : 637250 , nlumis : -1

        ]

skim_test_samples = [
    FilelistSample(
        filelist=["VBSWWH_C2V_4p5_RunIIAutumn18NanoAOD_VBSWWH_C2V_4p5_v3_ext1.root"], 
        dataset="/DataLakeSkimTestSampleVBSWWH/NANOAODSIM"
    ),
]
