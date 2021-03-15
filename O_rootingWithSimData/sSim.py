# Simulate data

if not var.gsl_rng:
    var.gsl_rng = pf.gsl_rng_get()
mySeed = 1956
pf.gsl_rng_set(var.gsl_rng, mySeed)

nTax = 5
taxNames = "A1 A2 A3 B1 B2".split()
a = func.newEmptyAlignment(dataType='dna', taxNames=taxNames, length=1200)
d = Data([a])

read('(((A1:0.4, A2:0.3):0.1, A3:0.5):0.15, (B1:0.5, B2:0.5):0.15);')
t = var.trees[0]
t.taxNames = taxNames

t.data = d

cA = t.newComp(free=1, spec='specified', val=[0.1, 0.2, 0.3], symbol='A')
cB = t.newComp(free=1, spec='specified', val=[0.2, 0.3, 0.4], symbol='B')
cR = t.newComp(free=1, spec='specified', val=[0.3, 0.4, 0.1], symbol='R')

t.setModelComponentOnNode(cA, t.root, clade=True)
t.setModelComponentOnNode(cB, t.node("B1").parent, clade=True)
t.setModelComponentOnNode(cR, t.root, clade=False)

t.newRMatrix(free=0, spec='ones')   # F81
t.setNGammaCat(nGammaCat=1)
#t.newGdasrv(free=0, val=0.5)
t.setPInvar(free=0, val=0.0)
t.draw(model=True)

t.simulate()

d.writeNexus('d.nex', writeDataBlock=True)
