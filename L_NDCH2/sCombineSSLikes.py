# Combine runs

def combineSSvals(rA, rB):
    llA = [l for l in open(f"mcmc_ssLikes_{rA}")] 
    llB = [l for l in open(f"mcmc_ssLikes_{rB}")]
    assert len(llA) == len(llB)
    llAB = []
    size = 2000
    start = 0
    end = start + size
    while 1:
        try:
            sVal = llA[start]
            llAB += llA[start:end]    
            llAB += llB[start:end]
            print(start,end)
            start += size
            end = start + size
        except IndexError:
            break
    fOut = open(f"mcmc_ssLikes_{rA}{rB}", "w")
    for it in llAB:
        print(it, end='', file=fOut)
    fOut.close()


combineSSvals(0, 1)
combineSSvals(2, 3)
