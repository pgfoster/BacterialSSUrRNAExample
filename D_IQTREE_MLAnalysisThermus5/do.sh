iqtree2 -s ../thermus5.nex -m JC+G4 -T 1 -redo --prefix jc -B 1000  --seed 473 
iqtree2 -s ../thermus5.nex -m TIM2+F+G4 -T 1 -redo --prefix tim2 -B 1000 --seed 947
iqtree2 -s ../thermus5.nex -m GTR+F+G4 -T 1 -redo --prefix gtr -B 1000 --seed 3367

