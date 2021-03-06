import FWCore.ParameterSet.Config as cms


mpblocks = cms.untracked.PSet(
    rxBlockLength    = cms.untracked.vint32(41,41,41,41, # q0 0-3
                                            41,41,41,41, # q1 4-7
                                            41,41,41,41, # q2 8-11
                                            41,41,41,41, # q3 12-15
                                            41,41,41,41, # q4 16-19
                                            41,41,41,41, # q5 20-23
                                            41,41,41,41, # q6 24-27
                                            41,41,41,41, # q7 28-31
                                            41,41,41,41, # q8 32-35
                                            41,41,41,41, # q9 36-39
                                            41,41,41,41, # q10 40-43
                                            41,41,41,41, # q11 44-47
                                            41,41,41,41, # q12 48-51
                                            41,41,41,41, # q13 52-55
                                            41,41,41,41, # q14 56-59
                                            41,41,41,41, # q15 60-63
                                            41,41,41,41, # q16 64-67
                                            41,41,41,41), # q17 68-71

    txBlockLength    = cms.untracked.vint32(39,39,39,39, # q0 0-3
                                            39,39,0,0, # q1 4-7
                                            0,0,0,0, # q2 8-11
                                            0,0,0,0, # q3 12-15
                                            0,0,0,0, # q4 16-19
                                            0,0,0,0, # q5 20-23
                                            0,0,0,0, # q6 24-27
                                            0,0,0,0, # q7 28-31
                                            0,0,0,0, # q8 32-35
                                            0,0,0,0, # q9 36-39
                                            0,0,0,0, # q10 40-43
                                            0,0,0,0, # q11 44-47
                                            0,0,0,0, # q12 48-51
                                            0,0,0,0, # q13 52-55
                                            0,0,0,0, # q14 56-59
                                            0,0,0,0, # q15 60-63
                                            0,0,0,0, # q16 64-67
                                            0,0,0,0) # q17 68-71
)

stage2MPRaw = cms.EDProducer(
    "MP7BufferDumpToRaw",
    rxFile           = cms.untracked.string("mp_rx_summary.txt"),
    txFile           = cms.untracked.string("mp_tx_summary.txt"),

    # input file type
    packetisedData   = cms.untracked.bool(True),

    # parameters for non-packetised data
    nFramesPerEvent  = cms.untracked.int32(41),
    nFramesOffset    = cms.untracked.vuint32(0,0,0,0,0,0,0,0,0,0,0,0),
    nFramesLatency   = cms.untracked.vuint32(0,0,0,0,0,0,0,0,0,0,0,0),

    # DAQ parameters
    fedId            = cms.untracked.int32(1360),
    eventType        = cms.untracked.int32(238),
    fwVersion        = cms.untracked.int32(255),
    lenSlinkHeader   = cms.untracked.int32(8),
    lenSlinkTrailer  = cms.untracked.int32(8),

    # HW parameters
    boardId          = cms.untracked.vint32( 1,2,3,4,5,6,7,8,9,10,11,12 ),
    mux              = cms.untracked.bool(True),
    muxOffset        = cms.untracked.int32(0),

    # these parameters specify the amount of data from each link to be
    # recorded in the FEDRawData object
    # if insufficient data is read from any channel to produce the
    # record, module will pad with zeros
    blocks           = cms.untracked.VPSet(
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
        mpblocks,
    )

)
