import os
import numpy as np
import pandas
import math
from sklearn.metrics import auc, roc_curve

f1 = open("CSAR_bal/gt.txt", 'r')
f2 = open("2isto1/output_obtained_2isto1_bal.txt", 'r')

lines1 = f1.read().splitlines()
lines2 = f2.read().splitlines()

d = {}

for line in lines1:
	arr = line.split(" ")
	#print(arr)
	d[arr[1] + arr[2]] = arr[0]

tp = 0
tn = 0
fp = 0
fn = 0

preds = []
actuals = []
for line in lines2[:-1]:
	
	arr = line.split(" ")

	if(float(arr[0]) >= 0.5 and d[arr[3] + arr[4]] == '1'):
		tp += 1
	elif(float(arr[0]) < 0.5 and d[arr[3] + arr[4]] == '0'):
		tn += 1
	elif(float(arr[0]) < 0.5 and d[arr[3] + arr[4]] == '1'):
		fn += 1
	elif(float(arr[0]) >= 0.5 and d[arr[3] + arr[4]] == '0'):
		fp += 1

	preds.append(float(arr[0]))
	actuals.append(d[arr[3] + arr[4]])


print(tp, tn, fp, fn)

print("Accuracy =", (tp + tn)/(fp + fn + tp + tn))
print("Sensitivity =", tp/(tp + fn))
print("Specificity =", tn/(tn + fp))
print("Precision =", tp/(tp+fp))
print("F1 score =", 2*tp/(2*tp + fp + fn))
print("MCC =", (tp*tn - fp*fn)/math.sqrt((tp + fp)*(tp + fn)*(tn + fp)*(tn + fn)))
fpr, tpr, thresholds = roc_curve(actuals, preds, pos_label='1')
print("AUC =", auc(fpr, tpr))