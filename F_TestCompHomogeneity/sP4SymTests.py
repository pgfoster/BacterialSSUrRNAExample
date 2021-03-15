a = func.readAndPop("../thermus5.nex")

(QB, QS, QR, PB, PS, PR) = a.matchedPairsTests()
for pmat in [PB,PS,PR]:
    pmat.writePhylip(digitsAfterDecimal=3)


a.symtestAsInIQTreeNaserKhdour(verbose=True)
