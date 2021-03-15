# Read them in ...
cpr = McmcCheckPointReader(theGlob='*100000')

if 1:
    for m in cpr.mm:
        t = m.treePartitions.consensus()
        for n in t.iterInternalsNoRoot():
            if n.br.support:
                n.name = f"{n.br.support * 100:.0f}"
        t.draw()


tpA = cpr.mm[0].treePartitions
tpB = cpr.mm[1].treePartitions
tpA.combineWith(tpB)
tpA.writeSplits()

tpA = cpr.mm[2].treePartitions
tpB = cpr.mm[3].treePartitions
tpA.combineWith(tpB)
tpA.writeSplits()


