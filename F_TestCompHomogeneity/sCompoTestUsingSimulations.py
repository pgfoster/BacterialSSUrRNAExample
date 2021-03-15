a = func.readAndPop("../thermus5.nex")

# Make a bionj tree
dm = a.pDistances()
t = dm.bionj()

# Optimize with a GTR+G model
d = Data([a])
t.data = d
t.newComp(free=1, spec='empirical')
t.newRMatrix(free=1, spec='ones')
t.setNGammaCat(nGammaCat=4)
t.newGdasrv(free=1, val=0.5)
t.setPInvar(free=0, val=0.0)
t.optLogLike()

t.compoTestUsingSimulations(nSims=200, doIndividualSequences=True, doChiSquare=True)

