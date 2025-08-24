import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8HadronizerFilter",
        maxEventsToPrint = cms.untracked.int32(1),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        filterEfficiency = cms.untracked.double(1.0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        comEnergy = cms.double(5360.),
        PythiaParameters = cms.PSet(
            parameterSets = cms.vstring('skip_hadronization'),
            skip_hadronization = cms.vstring('ProcessLevel:all = off',
                'Check:event = off')
            )
        )

kaonplusfilter = cms.EDFilter("MCSingleParticleFilter",
        Status = cms.untracked.vint32(1),
        MinPt = cms.untracked.vdouble(0.05),
        MinEta = cms.untracked.vdouble(-2.5),
        MaxEta = cms.untracked.vdouble(2.5),
        ParticleID = cms.untracked.vint32(321),
        )

kaonminusfilter = cms.EDFilter("MCSingleParticleFilter",
        Status = cms.untracked.vint32(1,),
        MinPt = cms.untracked.vdouble(0.05),
        MinEta = cms.untracked.vdouble(-2.5),
        MaxEta = cms.untracked.vdouble(2.5),
        ParticleID = cms.untracked.vint32(+321),
        )

ProductionFilterSequence = cms.Sequence(generator*kaonplusfilter*kaonminusfilter)
