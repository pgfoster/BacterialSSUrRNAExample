a = func.readAndPop("../thermus5.nex")
d = Data([a])
print("Doing the whole alignment ---")
ret = d.compoChiSquaredTest(verbose=True)
print("ret is ", ret)
print("\nDo individual sequences, using dof=3 --- ")
ret = d.compoChiSquaredTest(verbose=False, getRows=True)
seqValues = ret[0][3]
for sNum,s in enumerate(a.sequences):
    prob = func.chiSquaredProb(seqValues[sNum], 3)
    # print(f"{s.name:12}  X^2={seqValues[sNum]:6.2f}  P={prob:8.6f}")
    print(f"| {s.name:12} | {seqValues[sNum]:6.2f} | {prob:8.6f} |")
print("sum is ", sum(seqValues))









