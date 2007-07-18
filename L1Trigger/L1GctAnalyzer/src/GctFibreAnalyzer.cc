// -*- C++ -*-
//
// Package:    GctFibreAnalyzer
// Class:      GctFibreAnalyzer
// 
/**\class GctFibreAnalyzer GctFibreAnalyzer.cc L1Trigger/L1GctAnalzyer/src/GctFibreAnalyzer.cc

Description: Analyzer individual fibre channels from the source card.

*/
//
// Original Author:  Alex Tapper
//         Created:  Thu Jul 12 14:21:06 CEST 2007
// $Id$
//
//

// Include file
#include "L1Trigger/L1GctAnalyzer/interface/GctFibreAnalyzer.h"

// Data format
#include "DataFormats/L1GlobalCaloTrigger/interface/L1GctCollections.h"

GctFibreAnalyzer::GctFibreAnalyzer(const edm::ParameterSet& iConfig):
  m_fibreSource(iConfig.getUntrackedParameter<edm::InputTag>("FibreSource"))
{
}


GctFibreAnalyzer::~GctFibreAnalyzer()
{
}

void GctFibreAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  
  Handle<L1GctFibreCollection> fibre;
  iEvent.getByLabel(m_fibreSource,fibre);

  std::cout << "New event! " << fibre->size()<< " fibres" << std::endl;
   
  for (L1GctFibreCollection::const_iterator f=fibre->begin(); f!=fibre->end(); f++){
    std::cout << "data=" << f->data() 
              << " block=" << f->block() 
              << " index=" << f->index() 
              << " bx=" << f->bx()
              << std::endl;
  }   

//   uint32_t data() const { return data_; }
//   uint16_t block() const { return block_; }
//   uint16_t index() const { return index_; }
  
//   source card type = 0 for electron cards

//   source card local ID = source card type (+4 if RCt crate >=9)

//   source card logical ID = 8*(RCT phi region 0-8) + source card local ID

}


void GctFibreAnalyzer::beginJob(const edm::EventSetup&)
{
}

void GctFibreAnalyzer::endJob() 
{
}

