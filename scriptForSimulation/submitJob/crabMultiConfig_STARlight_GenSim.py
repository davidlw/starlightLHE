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
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'step1_STARlight_LHE_GenSim_cfg.py'
config.JobType.numCores = 1
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
#config.Data.publication = False

config.section_('Site')
config.Data.ignoreLocality = True
#config.Site.whitelist = ['T1_US_*','T2_US_*', 'T2_CH_CERN']
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
#        "STARlight_CohJpsi2MuMu_PbPb5TeV_LHE_GenSim_v1": { "InputFiles": "lheFileList/CohJpsi_lhe.txt", "PrimaryDataset": "STARlight_CohJpsi2MuMu_PbPb5TeV_GenFilter", "Memory": 2000, "RunTime": 1000 },
#        "STARlight_InCohJpsi2MuMu_PbPb5TeV_LHE_GenSim_v1": { "InputFiles": "lheFileList/InCohJpsi_lhe.txt", "PrimaryDataset": "STARlight_InCohJpsi2MuMu_PbPb5TeV_GenFilter", "Memory": 2000, "RunTime": 1000 },
#        "STARlight_CohPsi2SFeeddown2MuMu_PbPb5TeV_LHE_GenSim_v1": { "InputFiles": "lheFileList/CohPsi2SFeeddown_lhe.txt", "PrimaryDataset": "STARlight_CohPsi2SFeeddown2MuMu_PbPb5TeV_GenFilter", "Memory": 2000, "RunTime": 1000 },
#        "STARlight_CohPsi2S2MuMu_PbPb5TeV_LHE_GenSim_v1": { "InputFiles": "lheFileList/CohPsi2S_lhe.txt", "PrimaryDataset": "STARlight_CohPsi2S2MuMu_PbPb5TeV_GenFilter", "Memory": 2000, "RunTime": 1000 },
#        "STARlight_InCohPsi2S2MuMu_PbPb5TeV_LHE_GenSim_v1": { "InputFiles": "lheFileList/InCohPsi2S_lhe.txt", "PrimaryDataset": "STARlight_InCohPsi2S2MuMu_PbPb5TeV_GenFilter", "Memory": 2000, "RunTime": 1000 },
#        "STARlight_LowMassGammaGamma2MuMu_PbPb5TeV_LHE_GenSim_v1": { "InputFiles": "lheFileList/LowMassGammaGamma_lhe.txt", "PrimaryDataset": "STARlight_LowMassGammaGamma2MuMu_PbPb5TeV_GenFilter", "Memory": 2000, "RunTime": 1000 },

# 
        "STARlight_CohPhi2KKinOOAt5p36TeV_LHE_GenSim_v2": { "InputFiles": "lheFileList/CohPhi2KKinOOAt5p36TeV_lhe.txt", "PrimaryDataset": "STARlight_CohPhi2KKinOOAt5p36TeV_GenFilter", "Memory": 2000, "RunTime": 1000, "PSet": "step1_STARlight_LHE_GenSim_cfg.py" },
        "STARlight_CohPhi2KKinpOAt9p9TeV_LHE_GenSim_v2": { "InputFiles": "lheFileList/CohPhi2KKinpOAt9p9TeV_lhe.txt", "PrimaryDataset": "STARlight_CohPhi2KKinpOAt9p9TeV_GenFilter", "Memory": 2000, "RunTime": 1000, "PSet": "step1_STARlight_LHE_GenSim_pO_cfg.py" },
        "STARlight_CohPhi2KKinNeNeAt5p36TeV_LHE_GenSim_v2": { "InputFiles": "lheFileList/CohPhi2KKinNeNeAt5p36TeV_lhe.txt", "PrimaryDataset": "STARlight_CohPhi2KKinNeNeAt5p36TeV_GenFilter", "Memory": 2000, "RunTime": 1000, "PSet": "step1_STARlight_LHE_GenSim_NeNe_cfg.py" },        
        }

## Submit job for different datasets 
for key, val in dataMap.items():
    config.General.requestName = key
    config.JobType.maxMemoryMB = val["Memory"]
    config.JobType.maxJobRuntimeMin = val["RunTime"]
    config.JobType.psetName = val["PSet"]
#    config.Data.inputDataset = val["Dataset"]
    config.Data.userInputFiles = open(val["InputFiles"]).readlines() 
    config.Data.outputPrimaryDataset = val["PrimaryDataset"]
    config.Data.outputDatasetTag = config.General.requestName
    config.Data.outLFNDirBase = '/store/group/phys_heavyions/davidlw/starlight/GenSim/' 
    print("Submitting CRAB job for: "+val["InputFiles"])
    submit(config)
