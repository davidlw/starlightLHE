#!/bin/bash
date

cmsDriver.py Configuration/GenProduction/python/HINPbPbAutumn18GS_STARlight_fragment.py --filein /afs/cern.ch/user/d/davidlw/starlightLHE_Phi2KK/generateLHE/CohPhi2KKinOOAt5p36TeV/lheFiles/slight_CohPhi2KKinOOAt5p36TeV_0001.lhe --filetype LHE --fileout file:step1_STARlight_LHE_GenSim.root --mc --eventcontent RAWSIM --no_exec --datatier GEN-SIM --conditions 150X_mcRun3_2025_forOO_realistic_v9 --beamspot DBrealistic --step GEN,SIM --scenario HeavyIons --geometry DB:Extended --era Run3_2025_UPC_OXY --python_filename step1_STARlight_LHE_GenSim_cfg.py --no_exec -n 100

cmsDriver.py step2 --filein file:step1_STARlight_LHE_GenSim.root --fileout step2_STARlight_Digi.root --mc --eventcontent RAWSIM --pileup HiMixNoPU --datatier GEN-SIM-RAW --conditions 150X_mcRun3_2025_forOO_realistic_v9 --step DIGI:pdigi_hi_nogen,L1,DIGI2RAW,HLT:PIon --geometry DB:Extended --era Run3_2025_UPC_OXY --python_filename step2_STARlight_Digi_cfg.py --no_exec --customise_commands "process.RAWSIMoutput.outputCommands.extend(['keep *_mix_MergedTrackTruth_*', 'keep *Link*_simSiPixelDigis__*', 'keep *Link*_simSiStripDigis__*'])"

cmsDriver.py step3 --filein file:step2_STARlight_Digi.root --fileout step3_STARlight_Reco.root --mc --eventcontent AODSIM --datatier AODSIM --conditions 150X_mcRun3_2025_forOO_realistic_v9 --step RAW2DIGI,L1Reco,RECO --era Run3_2025_UPC_OXY --python_filename step3_STARlight_Reco_cfg.py --no_exec --customise_commands "process.AODSIMoutput.outputCommands.extend(['keep *_mix_MergedTrackTruth_*', 'keep *Link*_simSiPixelDigis__*', 'keep *Link*_simSiStripDigis__*', 'keep *_generalTracks__*', 'keep *_hiConformalPixelTracks__*', 'keep *_siPixelClusters__*', 'keep *_siStripClusters__*'])"

cmsDriver.py step4 --filein file:step3_STARlight_Reco.root --fileout step4_STARlight_miniAOD.root --mc --eventcontent MINIAODSIM --datatier MINIAODSIM --conditions 150X_mcRun3_2025_forOO_realistic_v9 --step PAT --geometry DB:Extended --era Run3_2025_UPC_OXY --python_filename step4_STARlight_miniAOD_cfg.py --no_exec


# for pO: 150X_mcRun3_2025_forpO_realistic_v9
# for NeNe: 150X_mcRun3_2025_forNeNe_realistic_v9
