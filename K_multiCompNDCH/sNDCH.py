var.PIVEC_MIN = 1.e-6
var.RATE_MIN = 1.e-6
var.BRLEN_MIN = 1.e-5
var.GAMMA_SHAPE_MIN = 0.15

rNum = int(var.argvAfterDoubleDash[0])

# Unusually, make it exactly repeatable by setting the two random
# number seeds.  This would generally not be done.
if rNum == 2:
    myGslRngSeed = 421
    myPyRandomSeed = 7593
elif rNum == 3:
    myGslRngSeed = 77
    myPyRandomSeed = 967
if not var.gsl_rng:
    var.gsl_rng = pf.gsl_rng_get()
pf.gsl_rng_set(var.gsl_rng, myGslRngSeed)
import random
random.seed(myPyRandomSeed)


read("../thermus5.nex")
d = Data()
t = func.randomTree(taxNames=d.taxNames)
t.data = d

# Fully parameterize the comps, including a comp for the root
for n in t.nodes:
    c = t.newComp(free=1, spec='empirical', symbol='-')
    t.setModelComponentOnNode(c, node=n, clade=0)

t.newRMatrix(free=1, spec='ones')
t.setNGammaCat(nGammaCat=4)
t.newGdasrv(free=1, val=0.5)
t.setPInvar(free=0, val=0.0)

# Set up the MCMC
nGen = 200000
nSamples = 2000
sInterv = int(nGen / nSamples)
nCheckPoints = 2
cpInterv = int(nGen / nCheckPoints)

# Instantiate an Mcmc object.  Adjust nChains and runNum appropriately.
m = Mcmc(t, nChains=1, runNum=rNum, sampleInterval=sInterv, checkPointInterval=cpInterv, simulate=2)

m.prob.compLocation = 0.0
m.run(nGen)

