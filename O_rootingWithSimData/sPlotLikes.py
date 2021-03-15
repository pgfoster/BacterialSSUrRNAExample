if 1:
    dd = []
    for rNum in range(2):
        n = Numbers(f"mcmc_likes_{rNum}", col=1, skip=0)
        d = n.data[-1000:]
        #d = n.data[:]
        dd += d
    n = Numbers(dd)
    n.plot()

if 0:
    dd = []
    for rNum in range(2):
        n = Numbers(f"mcmc_hypers_{rNum}", col=1, skip=0)
        d = n.data[-1000:]
        #d = n.data[:]
        dd += d
    n = Numbers(dd)
    n.plot()
    dd = []
    for rNum in range(2):
        n = Numbers(f"mcmc_hypers_{rNum}", col=2, skip=0)
        d = n.data[-1000:]
        #d = n.data[:]
        dd += d
    n = Numbers(dd)
    n.plot()
