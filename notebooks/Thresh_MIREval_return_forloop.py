import mir_eval
import pandas as pd
import numpy as np
import Paths as p
import matplotlib.pyplot as plt

def threshold(unit, start_time, end_time, thresh):
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_peaks.npy"
    threshold_peaks = []
    predicted = []
    groundValues = []
    for i in np.load(checkFile):
        if (i[0]>=thresh):
            threshold_peaks.append(i)
            predicted.append(i[1]) 
    
    truth = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".txt"

    for line in open(truth,'r'):
        line = line.strip('\n')
        line = float(line) - 38340
        groundValues.append(line)
        
    groundValues = np.array(groundValues)
    predicted = np.array(predicted)
    
    
    
    F, P, R = mir_eval.onset.f_measure(groundValues,predicted) #(reference_onsets, estimated_onsets)
    
    return F,P,R



thresh_vals = []
x = 0
while (x<1):
    thresh_vals.append(x)
    x += 0.01

precision = []
recall = []
for i in thresh_vals:
    F, P, R = threshold(1,38340,38400,i)
    precision.append(P)
    recall.append(R)
    
plt.plot(recall,precision)
plt.ylabel('Precision')
plt.xlabel('Recall')
plt.show()    


