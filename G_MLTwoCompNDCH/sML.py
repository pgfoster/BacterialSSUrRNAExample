var.PIVEC_MIN = 1.e-6
var.RATE_MIN = 1.e-6
var.BRLEN_MIN = 1.e-5
var.GAMMA_SHAPE_MIN = 0.15

read("../thermus5.nex")
d = Data()

if 1:
    # Rooted on a trifurcating  internal node
    tTrue = func.readAndPop("((Aquifex, Thermotoga), Bacillus, (Thermus, Deinococcus));")
    tTrue.reRoot(tTrue.node("Bacillus").parent)
    tAttract = func.readAndPop("((Aquifex, Thermotoga), Thermus, (Bacillus, Deinococcus));")
    tAttract.reRoot(tAttract.node("Bacillus").parent)
else:
    # If bifurcating, rooted on the branch to Bacillus --- we get the same results as above
    tTrue = func.readAndPop("(Bacillus, ((Aquifex, Thermotoga), (Deinococcus, Thermus)));")
    tAttract = func.readAndPop("(Bacillus, (Deinococcus, ((Aquifex, Thermotoga), Thermus)));")

likesOut = open("likes", "w") 
for mNm in ["gtr", "ndch"]:
    for t in (tTrue, tAttract):
        t.data = d

        # for both "gtr" and "ndch"
        A = t.newComp(free=1, spec='empirical', symbol='A')

        if mNm == "ndch":
            B = t.newComp(free=1, spec='empirical', symbol='B')

            t.setModelComponentOnNode(A, t.root, clade=True)
            t.setModelComponentOnNode(B, t.node("Bacillus"), clade=False)
            t.setModelComponentOnNode(B, t.node("Deinococcus"), clade=False)

        t.newRMatrix(free=1, spec='ones')
        t.setNGammaCat(nGammaCat=4)
        t.newGdasrv(free=1, val=0.5)
        t.setPInvar(free=0, val=0.0)

        if t == tTrue:
            tNm = "tTrue"
        elif t == tAttract:
            tNm = "tAttract"
        t.name = f"{tNm}_{mNm}"
        t.optLogLike(method="BOBYQA", verbose=False)
        print(f"{t.name:15s} {t.logLike:.2f}")
        print(f"{t.name:15s} {t.logLike:.2f}", file=likesOut)
        t.tPickle()
        t.model = None


