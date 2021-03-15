a = func.readAndPop("../thermus.nex")
# 1273 sites, 815 constant sites

d = Data([a])
d.compoSummary()

for sNum,s in enumerate(a.sequences):
    comp = a.composition(sequenceNumberList=[sNum])
    cg = comp[1] + comp[2]
    print(f"{s.name:12}  {100 * cg:0.0f}")


print("\n\nBelow with no constant sites ------")
m = a.constantMask() 
a = a.subsetUsingMask(m, inverse=True)
# a.writeNexus("noConstantSites.nex")
d = Data([a])
d.compoSummary()

for sNum,s in enumerate(a.sequences):
    comp = a.composition(sequenceNumberList=[sNum])
    cg = comp[1] + comp[2]
    print(f"{s.name:12}  {100 * cg:0.0f}")



a = func.readAndPop("../thermus5.nex")
# 1273 sites, 835 constant sites

d = Data([a])
d.compoSummary()

for sNum,s in enumerate(a.sequences):
    comp = a.composition(sequenceNumberList=[sNum])
    cg = comp[1] + comp[2]
    print(f"{s.name:12}  {100 * cg:0.0f}")


print("\n\nBelow with no constant sites ------")
m = a.constantMask() 
a = a.subsetUsingMask(m, inverse=True)
# a.writeNexus("noConstantSites.nex")
d = Data([a])
d.compoSummary()

for sNum,s in enumerate(a.sequences):
    comp = a.composition(sequenceNumberList=[sNum])
    cg = comp[1] + comp[2]
    print(f"{s.name:12}  {100 * cg:0.0f}")
