read("../thermus5.nex")
d = Data()
ret = d.compoChiSquaredTest()
originalChSq = ret[0][0]

dd = []
for rNum in [0,1]:
    n = Numbers(f"mcmc_sims_{rNum}", col=1, skip=0)
    d = n.data[-1000:]
    #d = n.data[:]
    dd += d
n = Numbers(dd)
n.plot()

n.tailAreaProbability(originalChSq, verbose=1)



