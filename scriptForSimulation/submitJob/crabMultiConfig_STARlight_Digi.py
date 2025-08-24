import importlib, sys

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from http.client import HTTPException  # updated import for Python 3

# We want to put all the CRAB project directories from the tasks we submit here into one common directory.
# That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'step2_STARlight_Digi_cfg.py'
config.JobType.numCores = 1
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True

config.section_('Site')
config.Data.ignoreLocality = True
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_US_MIT'
#config.Site.storageSite = 'T3_US_Rice'

def submit(config):
    try:
        crabCommand('submit', config = config, dryrun=False)
    except HTTPException as hte:
        print("Failed submitting task: %s" % (hte.headers))  # updated for Python 3

    except ClientException as cle:
        print("Failed submitting task: %s" % (cle))  # updated for Python 3

#############################################################################################
## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
#############################################################################################

dataMap = {
#            "STARlight_CohJpsi2MuMu_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_CohJpsi2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_CohJpsi2MuMu_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },
#            "STARlight_InCohJpsi2MuMu_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_InCohJpsi2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_InCohJpsi2MuMu_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },
#            "STARlight_CohPsi2SFeeddown2MuMu_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_CohPsi2SFeeddown2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_CohPsi2SFeeddown2MuMu_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },
#            "STARlight_CohPsi2S2MuMu_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_CohPsi2S2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_CohPsi2S2MuMu_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },
#            "STARlight_InCohPsi2S2MuMu_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_InCohPsi2S2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_InCohPsi2S2MuMu_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },
#            "STARlight_LowMassGammaGamma2MuMu_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_LowMassGammaGamma2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_LowMassGammaGamma2MuMu_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },
#            "STARlight_CohJpsi2MuMu_0n0n_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_CohJpsi2MuMu_0n0n_PbPb5TeV_GenFilter/shuaiy-STARlight_CohJpsi2MuMu_0n0n_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },
#            "STARlight_CohJpsi2MuMu_0nXn_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_CohJpsi2MuMu_0nXn_PbPb5TeV_GenFilter/shuaiy-STARlight_CohJpsi2MuMu_0nXn_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },
#            "STARlight_CohJpsi2MuMu_XnXn_PbPb5TeV_Digi_v1": { "Dataset": "/STARlight_CohJpsi2MuMu_XnXn_PbPb5TeV_GenFilter/shuaiy-STARlight_CohJpsi2MuMu_XnXn_PbPb5TeV_LHE_GenSim_v1-ea02cbb416162d6ecc01cf3ce88dbce2/USER", "Memory": 2500, "RunTime": 1000 },

# 
            "STARlight_CohPhi2KKinOOAt5p36TeV_LHE_Digi_v2": { "Dataset": "/STARlight_CohPhi2KKinOOAt5p36TeV_GenFilter/phys_heavyions-STARlight_CohPhi2KKinOOAt5p36TeV_LHE_GenSim_v2-2e0df07983baa50024dc1ff099ed6ef4/USER", "Memory": 4500, "RunTime": 1000, "PSet": "step2_STARlight_Digi_cfg.py" },
            "STARlight_CohPhi2KKinpOAt9p9TeV_LHE_Digi_v2": { "Dataset": "/STARlight_CohPhi2KKinpOAt9p9TeV_GenFilter/phys_heavyions-STARlight_CohPhi2KKinpOAt9p9TeV_LHE_GenSim_v2-8ec37417ad9be5812f7cb8743d107335/USER", "Memory": 4500, "RunTime": 1000, "PSet": "step2_STARlight_Digi_pO_cfg.py" },
            "STARlight_CohPhi2KKinNeNeAt5p36TeV_LHE_Digi_v2": { "Dataset": "/STARlight_CohPhi2KKinNeNeAt5p36TeV_GenFilter/phys_heavyions-STARlight_CohPhi2KKinNeNeAt5p36TeV_LHE_GenSim_v2-b1a0bb0b5304466358871391e9f9d1f4/USER", "Memory": 4500, "RunTime": 1000, "PSet": "step2_STARlight_Digi_NeNe_cfg.py" },
            }

## Submit job for different datasets 
for key, val in dataMap.items():
    config.General.requestName = key
    config.JobType.maxMemoryMB = val["Memory"]
    config.JobType.maxJobRuntimeMin = val["RunTime"]
    config.JobType.psetName = val["PSet"]    
    config.Data.inputDataset = val["Dataset"]
    config.Data.outputDatasetTag = config.General.requestName
    config.Data.outLFNDirBase = '/store/group/phys_heavyions/davidlw/starlight/DigiRaw/'
    print("Submitting CRAB job for: "+val["Dataset"])

    # --- workaround to avoid CMSSW config caching ---
    if 'cmsRun' in sys.modules:
        del sys.modules['cmsRun']
    if 'FWCore.ParameterSet.Config' in sys.modules:
        del sys.modules['FWCore.ParameterSet.Config']

    submit(config)
