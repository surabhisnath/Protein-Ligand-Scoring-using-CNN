import os
import numpy as np
import pandas
import math

f1 = open("General_train/gt.txt", 'r')
f2 = open("Affinity_General/output_obtained_general.txt", 'r')

lines1 = f1.read().splitlines()
lines2 = f2.read().splitlines()

d = {}

for line in lines1:
	arr = line.split(" ")
	#print(arr)
	d[arr[2] + arr[3]] = arr[1]


loss = 0
sq = 0
for line in lines2:
	arr = line.split(" ")
	temp = abs(float(d[arr[5] + arr[6]])) - abs(float(arr[1]))
	loss += temp
	sq += temp*temp

print(len(lines2))
print("RMSD =", math.sqrt(sq/len(lines2)))
print("Avg loss =", loss/len(lines2))