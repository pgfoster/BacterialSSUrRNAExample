# tAttract_gtr.p4_tPickle
# tAttract_ndch.p4_tPickle
# tTrue_gtr.p4_tPickle
# tTrue_ndch.p4_tPickle

read('../thermus5.nex')
d = Data()
nReps = 113

print("Doing sims and opts.  This can take some time ...")

t = func.readAndPop('tAttract_gtr.p4_tPickle')
t.data = d
mySeed = 2639
t.simsForModelFitTests(reps=nReps, seed=mySeed)
mySimsFileName = f"sims_CompStats_{mySeed}"
# Warning -- the test uses all the sims files that it finds.  Don't get mixed up.
t.modelFitTests(fName='tamcft_Attract_gtr')
os.system(f"mv {mySimsFileName} finished_sims_{mySeed}")


t = func.readAndPop('tTrue_gtr.p4_tPickle')
t.data = d
mySeed = 93476
t.simsForModelFitTests(reps=nReps, seed=mySeed)
mySimsFileName = f"sims_CompStats_{mySeed}"
t.modelFitTests(fName='tamcft_True_gtr')
os.system(f"mv {mySimsFileName} finished_sims_{mySeed}")


t = func.readAndPop('tAttract_ndch.p4_tPickle')
t.data = d
mySeed = 235
t.simsForModelFitTests(reps=nReps, seed=mySeed)
mySimsFileName = f"sims_CompStats_{mySeed}"
t.modelFitTests(fName='tamcft_Attract_ndch')
os.system(f"mv {mySimsFileName} finished_sims_{mySeed}")

t = func.readAndPop('tTrue_ndch.p4_tPickle')
t.data = d
mySeed = 429
t.simsForModelFitTests(reps=nReps, seed=mySeed)
mySimsFileName = f"sims_CompStats_{mySeed}"
t.modelFitTests(fName='tamcft_True_ndch')
os.system(f"mv {mySimsFileName} finished_sims_{mySeed}")

