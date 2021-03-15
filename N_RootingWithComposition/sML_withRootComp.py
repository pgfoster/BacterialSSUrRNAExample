var.PIVEC_MIN = 1.e-6
var.RATE_MIN = 1.e-6
var.BRLEN_MIN = 1.e-5
var.GAMMA_SHAPE_MIN = 0.15

read("../thermus5.nex")
d = Data()

tTrue = func.readAndPop("(Aquifex, Thermotoga, (Bacillus, (Thermus, Deinococcus)));")
tTrue.taxNames = d.taxNames
print("\n\nMake trees with roots on all 7 branches on this tree ...")
tTrue.draw()

tt = tTrue.allBiRootedTrees()
for i,t in enumerate(tt.trees):
    t.name = f"r{i + 1}"

# var.newtAndBrentPowellOptPassLimit=200

likeDict = {}
maxLikeOverRoots = None
mlTree = None

for t in tt.trees:
    t.data = d

    A = t.newComp(free=1, spec='empirical', symbol='A')
    B = t.newComp(free=1, spec='empirical', symbol='B')
    R = t.newComp(free=1, spec='empirical', symbol='R')

    t.setModelComponentOnNode(A, t.root, clade=True)
    t.setModelComponentOnNode(B, t.node("Bacillus"), clade=False)
    t.setModelComponentOnNode(B, t.node("Deinococcus"), clade=False)
    t.setModelComponentOnNode(R, t.root, clade=False)

    t.newRMatrix(free=1, spec='ones')
    t.setNGammaCat(nGammaCat=4)
    t.newGdasrv(free=1, val=0.5)
    t.setPInvar(free=0, val=0.0)

    t.optLogLike(method="BOBYQA", verbose=False)
    print(f"{t.name:15s} {t.logLike:.2f}")
    likeDict[t.name] = t.logLike
    try:
        if t.logLike > maxLikeOverRoots:
            maxLikeOverRoots = t.logLike
            mlTree = t
    except TypeError:   # maxLikeOverRoots is None
        maxLikeOverRoots = t.logLike
        mlTree = t
    #t.tPickle()
    t.model = None
    t.data = None


print(f"The ML root is {mlTree.name:15s} {mlTree.logLike:.2f}")
mlTree.draw()


