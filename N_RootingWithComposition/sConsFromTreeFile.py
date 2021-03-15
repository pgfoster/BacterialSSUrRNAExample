tp = TreePartitions("mcmc_trees_0.nex", skip=1000)
t = tp.consensus(showRootInfo=True)
for n in t.iterInternalsNoRoot():
    if n.br.support:
        n.name = f"{n.br.support * 100:.0f}"
t.draw()

tp = TreePartitions("mcmc_trees_1.nex", skip=1000)
t = tp.consensus(showRootInfo=True)
for n in t.iterInternalsNoRoot():
    if n.br.support:
        n.name = f"{n.br.support * 100:.0f}"
t.draw()
