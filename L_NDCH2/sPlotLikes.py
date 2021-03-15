if 1:
    dd = []
    for rNum in range(4):
        n = Numbers(f"mcmc_likes_{rNum}", col=1, skip=0)
        d = n.data[-1000:]
        #d = n.data[:]
        dd += d
    n = Numbers(dd)
    n.plot()

