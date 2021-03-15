dd = []
for rNum in [2,3]:
    n = Numbers(f"mcmc_hypers_{rNum}", col=1, skip=0)
    d = n.data[-1000:]
    #d = n.data[:]
    dd += d
n = Numbers(dd)
n.plot()

dd = []
for rNum in [2,3]:
    n = Numbers(f"mcmc_hypers_{rNum}", col=2, skip=0)
    d = n.data[-1000:]
    #d = n.data[:]
    dd += d
n = Numbers(dd)
n.plot()

