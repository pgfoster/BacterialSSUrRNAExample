import random
random.seed(210)

a = func.readAndPop(f"../thermus5.nex")
tt = []
for rNum in range(200):
    b = a.bootstrap()
    dm = b.compositionEuclideanDistanceMatrix()
    t = dm.bionj()
    tt.append(t)
tp = TreePartitions(tt, taxNames=a.taxNames)
tp.writeSplits()
t = tp.consensus()
for n in t.iterInternalsNoRoot():
    n.name = "%.0f" % (100. * n.br.support)
t.writeNexus(f"thermusCompoCons.nex")
t.draw()


