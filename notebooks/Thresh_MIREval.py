import mir_eval
import pandas as pd
import numpy as np
import Paths as p

def threshold(unit, start_time, end_time, thresh):
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_peaks.npy"
    threshold_peaks = []
    predicted = []
    groundValues = []
    for i in np.load(checkFile):
        if (i[0]>thresh):
            threshold_peaks.append(i)
            predicted.append(i[1]) #+38340)
    
    truth = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".txt"
    

    for line in open(truth,'r'):
        line = line.strip('\n')
        line = float(line) - 38340
        groundValues.append(line)

    groundValues = np.array(groundValues)
    predicted = np.array(predicted)
    
    F, P, R = mir_eval.onset.f_measure(groundValues,predicted) #(reference_onsets, estimated_onsets)

    
    print("F-Measure: " + str(F))
    print("Precision: " + str(P))
    print("Recall: "+ str(R))
    print("***********************")


tresh_vals = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.5]
for i in tresh_vals:
    print("Threshold is: "+str(i))
    threshold(1,38340,38400,i)





