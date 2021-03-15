import math
# Restart an MCMC from a checkpoint.

# Settings made to the var module in the original MCMC are not in
# the pickled file, so you will probably need to set them again ---
var.PIVEC_MIN = 1.e-6
var.RATE_MIN = 1.e-6
var.BRLEN_MIN = 1.e-5
var.GAMMA_SHAPE_MIN = 0.15

read("../thermus5.nex")
d = Data()


# Assuming more than one run, we set the run number by calling this script as
# p4 sRestartMcmc.py -- 0     # eg 0, 1, 2, ...
rNum = int(var.argvAfterDoubleDash[0])

m = func.unPickleMcmc(rNum, d)

# You probably don't want to do this, but 
# it is possible to change the mcmc here.
# eg
# m.sampleInterval = 200

m.doSteppingStone = True

alpha = 0.25
K = 8
bb = [math.pow((k/K),(1/alpha)) for k in range(K)]
bb.reverse()
print("bb ", bb)

for b in bb:
    m.ssBeta = b
    m.run(20000, writeSamples=False)  # sort of a "burnin" when steps change
    m.run(m.sampleInterval * 1000, writeSamples=True)
    
