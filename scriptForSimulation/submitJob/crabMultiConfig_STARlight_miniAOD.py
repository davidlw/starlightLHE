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
#config.JobType.psetName = 'step4_STARlight_miniAOD_cfg.py'
config.JobType.numCores = 1
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
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
#            "STARlight_CohJpsi2MuMu_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_CohJpsi2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_CohJpsi2MuMu_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },
#            "STARlight_InCohJpsi2MuMu_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_InCohJpsi2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_InCohJpsi2MuMu_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },
#            "STARlight_CohPsi2SFeeddown2MuMu_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_CohPsi2SFeeddown2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_CohPsi2SFeeddown2MuMu_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },
#            "STARlight_CohPsi2S2MuMu_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_CohPsi2S2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_CohPsi2S2MuMu_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },
#            "STARlight_InCohPsi2S2MuMu_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_InCohPsi2S2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_InCohPsi2S2MuMu_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },
#            "STARlight_LowMassGammaGamma2MuMu_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_LowMassGammaGamma2MuMu_PbPb5TeV_GenFilter/shuaiy-STARlight_LowMassGammaGamma2MuMu_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },
#            "STARlight_CohJpsi2MuMu_0n0n_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_CohJpsi2MuMu_0n0n_PbPb5TeV_GenFilter/shuaiy-STARlight_CohJpsi2MuMu_0n0n_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },
#            "STARlight_CohJpsi2MuMu_0nXn_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_CohJpsi2MuMu_0nXn_PbPb5TeV_GenFilter/shuaiy-STARlight_CohJpsi2MuMu_0nXn_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },
#            "STARlight_CohJpsi2MuMu_XnXn_PbPb5TeV_Reco_v1": { "Dataset": "/STARlight_CohJpsi2MuMu_XnXn_PbPb5TeV_GenFilter/shuaiy-STARlight_CohJpsi2MuMu_XnXn_PbPb5TeV_Digi_v1-c652f3d0771ac294a6a8110896e6f94d/USER", "Memory": 2000, "RunTime": 1000 },

#
            "STARlight_CohPhi2KKinOOAt5p36TeV_LHE_miniAOD_v2": { "Dataset": "", "Memory": 2500, "RunTime": 1000, "PSet": "step4_STARlight_miniAOD_cfg.py" },
            "STARlight_CohPhi2KKinpOAt9p9TeV_LHE_miniAOD_v2": { "Dataset": "", "Memory": 2500, "RunTime": 1000, "PSet": "step4_STARlight_miniAOD_pO_cfg.py" },
            "STARlight_CohPhi2KKinNeNeAt5p36TeV_LHE_miniAOD_v2": { "Dataset": "", "Memory": 2500, "RunTime": 1000, "PSet": "step4_STARlight_miniAOD_NeNe_cfg.py" },            
            }

## Submit job for different datasets 
for key, val in dataMap.items():
    config.General.requestName = key
    config.JobType.maxMemoryMB = val["Memory"]
    config.JobType.maxJobRuntimeMin = val["RunTime"]
    config.JobType.psetName = val["PSet"]
    config.Data.inputDataset = val["Dataset"]
    config.Data.outputDatasetTag = config.General.requestName
    config.Data.outLFNDirBase = '/store/group/phys_heavyions/davidlw/starlight/miniAOD/'
    print("Submitting CRAB job for: "+val["Dataset"])
    submit(config)
