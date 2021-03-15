# tAttract_gtr.p4_tPickle
# tAttract_ndch.p4_tPickle
# tTrue_gtr.p4_tPickle
# tTrue_ndch.p4_tPickle
# consel(rankByInputOrder=False, clobber=False, quiet=1, tidy=1, returnResults=False, seed=0)
# http://p4.nhm.ac.uk/modules/trees.html?highlight=consel#p4.trees.Trees.consel

read("../thermus5.nex")
d = Data()
for mNm in ['gtr', 'ndch']:
    var.trees = []
    if mNm == 'gtr':
        read("tAttract_gtr.p4_tPickle")
        read("tTrue_gtr.p4_tPickle")
    elif mNm == 'ndch':
        read("tAttract_ndch.p4_tPickle")
        read("tTrue_ndch.p4_tPickle")

    tAttract = var.trees[0]
    tAttract.data = d
    tTrue = var.trees[1]
    tTrue.data = d

    tt = Trees()
    tt.consel(seed=135)                          # unusually, set the seed, to make it repeatable
    os.system("mv conselOut %s_conselOut" % mNm)
