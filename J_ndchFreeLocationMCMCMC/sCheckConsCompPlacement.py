from p4.treefilelite import TreeFileLite

# Use the TreeFileLite class to get individual tree strings from the
# Mcmc output.

if 1:
    # Duplicate the TreeFileLite.getTree method, rename it getTreeM,
    # and modify it so that it will use
    # t.parseNexus(doModelComments=1)
    def getTreeM(self, treeNum):
        tLine = self.tLines[treeNum]
        if self.verbose >= 3:
            print(tLine)
        f = io.StringIO(tLine)
        t = Tree()
        if tLine.startswith("("):
            t.parseNewick(f, translationHash=self.translationHash)
            t.setPreAndPostOrder()
        else:
            t.parseNexus(f, translationHash=self.translationHash, doModelComments=1)
        return t
    TreeFileLite.getTreeM = getTreeM


# Look at what compNum is attached to the Deinococcus leaf node, from
# trees 200 -- 2000.

for rNum in [2,3]:
    tfl = TreeFileLite(f"mcmc_trees_{rNum}.nex")
    cNums = [0, 0]
    for tNum in range(200,2000):
        t = tfl.getTreeM(tNum)
        n = t.node("Deinococcus")
        cNum = n.parts[0].compNum
        cNums[cNum] += 1
    print(f"For rNum {rNum}, Deinococcus had compNums: ", cNums)
