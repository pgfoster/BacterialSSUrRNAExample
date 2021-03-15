a = func.readAndPop("../thermus.nex")
a.dump()
a.makeSequenceForNameDict()
s = a.sequenceForNameDict["T_ruber"]
a.sequences.remove(s)
a.dump()
a.writePhylip("../thermus5.phy")
a.writeNexus("../thermus5.nex")
