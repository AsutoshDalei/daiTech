class bill:
    def __init__(self):
        self.labourTot = 0
        self.subContractorTot = 0
        self.licensingTot = 0
        self.elecServiceTot = 0
        self.wallTot = 0
        self.outdoorTot = 0
        self.evceTot = 0
        self.materialsPre, self.concretePre, self.evcePre = 0, 0, 0
        self.preTaxTot = 0
        self.preServiceFeeTot = 0
        self.grandTotal = 0
        self.markup = {'laborPre':0.3, 'subcontractPre':0.3, 'materialsPre':0.3, 'concretePre':0.3, 'evcePre':0.22}
        self.taxMap = {'DC':0.06,'MD':0.06, 'VA':0.053}


    def labourCalc(self,labourJson):
        for lb in labourJson:
            self.labourTot += labourJson[lb]['amount']*labourJson[lb]['hours']
    def subContractorCalc(self, subContractorJson):
        for sb in subContractorJson:
            self.subContractorTot += subContractorJson[sb]['amount']*subContractorJson[sb]['units']
    def licensingCalc(self, permitJson):
        for pr in permitJson:
            self.licensingTot += permitJson[pr]['amount']*permitJson[pr]['units']
    def elecServiceCalc(self, materialJson):
        for mt in materialJson:
            self.elecServiceTot += materialJson[mt]['amount']*materialJson[mt]['units']
            # print(materialJson[mt]['amount']*materialJson[mt]['units'])
    def wallCalc(self, wallPenetrationJson):
        for wl in wallPenetrationJson:
            self.wallTot += wallPenetrationJson[wl]['amount']*wallPenetrationJson[wl]['units']
    def outdoorCalc(self, addOnJson):
        for ot in addOnJson:
            self.outdoorTot += addOnJson[ot]['amount']*addOnJson[ot]['units']
    def evceCalc(self, evceJson):
        for ev in evceJson:
            self.evceTot += evceJson[ev]['amount']*evceJson[ev]['units']

    def preTaxCalc(self):
        laborPre = self.labourTot/(1-self.markup['laborPre'])
        subcontractPre = self.subContractorTot/(1-self.markup['subcontractPre'])
        self.materialsPre = (self.elecServiceTot+self.wallTot)/(1-self.markup['materialsPre'])
        self.concretePre = (self.outdoorTot+self.wallTot)/(1-self.markup['concretePre'])
        self.evcePre = self.evceTot/(1-self.markup['evcePre'])

        self.preTaxTot = laborPre + subcontractPre + self.materialsPre + self.concretePre + self.evcePre
        # print(f"PreTaxTotal: {self.preTaxTot:.2f}")

    def finalCalcs(self, state='VA', permit=600, referralQmerit=0.12):
        stateTax = self.taxMap[state] * (self.materialsPre+self.concretePre+self.evcePre)
        # print(f"stateTaxTotal: {stateTax:.2f}")
        self.preServiceFeeTot = stateTax + permit + self.preTaxTot

        referralFee = (self.preTaxTot+stateTax)*referralQmerit
        self.grandTotal = self.preServiceFeeTot + referralFee

        return self.grandTotal


# try:
#     sample = bill()
#     sample.labourCalc(labourJson)

#     sample.subContractorCalc(subContractorJson)

#     sample.licensingCalc(permitJson)
#     sample.elecServiceCalc(materialJson)
#     sample.wallCalc(wallPenetrationJson)
#     sample.outdoorCalc(addOnJson)
#     sample.evceCalc(evceJson)

#     sample.preTaxCalc()
#     grandTot = sample.finalCalcs(permit=425, state='VA')
#     print('1.',sample.labourTot)
#     print('2.',sample.subContractorTot)
#     print('3.',sample.licensingTot)
#     print('4.',sample.elecServiceTot)
#     print('5.',sample.wallTot)
#     print('6.',sample.outdoorTot)
#     print('7.',sample.evceTot)
#     print(f"Grand Total: ${grandTot:.2f}",)

# except Exception as e:
#     print("ERR", e)
