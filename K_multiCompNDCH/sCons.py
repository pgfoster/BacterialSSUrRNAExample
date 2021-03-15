# Read them in ...
cpr = McmcCheckPointReader(theGlob='*200000')

if 1:
    for m in cpr.mm:
        t = m.treePartitions.consensus(showRootInfo=True)
        for n in t.iterInternalsNoRoot():
            if n.br.support:
                n.name = f"{n.br.support * 100:.0f}"
        t.draw()



print("NDCH splits")
tpA = cpr.mm[0].treePartitions
tpB = cpr.mm[1].treePartitions
tpA.combineWith(tpB)
tpA.writeSplits()

