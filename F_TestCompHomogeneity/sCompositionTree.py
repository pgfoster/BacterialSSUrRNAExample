# The bootstrap below uses the Python random module.  You would not
# normally do this, but to make it exactly repeatable you can set the
# random seed.  That is done here
import random
random.seed(57)

doRemoveConstSites = False

if 1:
    a = func.readAndPop("../thermus.nex")
    if doRemoveConstSites:
        m = a.constantMask() 
        a = a.subsetUsingMask(m, inverse=True)
        # a.writeNexus("noConstantSites.nex")

    # bootstrap the data
    tt = []
    for bNum in range(200):
        b = a.bootstrap()
        # make a distance matrix from composition
        dm = b.compositionEuclideanDistanceMatrix()
        # tree out those distances using bionj (which needs to be installed)
        t = dm.bionj()
        tt.append(t)

    tp = TreePartitions(tt, taxNames=a.taxNames)
    conTree = tp.consensus()
    for n in conTree.iterInternalsNoRoot():
        n.name = "%.0f" % (100. * n.br.support)
    conTree.draw()
    print()

if 1:
    a = func.readAndPop("../thermus5.nex")
    if doRemoveConstSites:
        m = a.constantMask() 
        a = a.subsetUsingMask(m, inverse=True)
        # a.writeNexus("noConstantSites.nex")

    # bootstrap the data
    tt = []
    for bNum in range(200):
        b = a.bootstrap()
        # make a distance matrix from compositions
        dm = b.compositionEuclideanDistanceMatrix()
        # tree out those distances using bionj (which needs to be installed)
        t = dm.bionj()
        tt.append(t)

    tp = TreePartitions(tt, taxNames=a.taxNames)
    conTree = tp.consensus()
    for n in conTree.iterInternalsNoRoot():
        n.name = "%.0f" % (100. * n.br.support)
    conTree.draw()
    conTree.write()

    
