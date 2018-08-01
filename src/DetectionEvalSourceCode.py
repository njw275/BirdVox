import Paths as p
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mir_eval
import librosa
import os
import sox

def onset(unit, start_time,fmin_input,h_length):
    if (start_time == 0):
        end_time = 605
    else:
        end_time = start_time+610
        
    duration_length = end_time - start_time
    
    file = p.get_trimmed_audio() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".wav"

    y, sr = librosa.load(file, duration=duration_length)
    
    D = librosa.stft(y)
    times = librosa.frames_to_time(np.arange(D.shape[1]))
    
    onset_env = librosa.onset.onset_strength(y=y, sr=sr,fmin=fmin_input,hop_length=h_length)    #,fmin=1000)

    print(onset_env)
    saveFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_detections"
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_detections.npy"
    np.save(saveFile, onset_env)
    
def peak_picking(unit, start_time):      #checkFile):
    if (start_time == 0):
        end_time = 605
    else:
        end_time = start_time+610
        
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_detections.npy"
    li = np.load(checkFile) 
    peaks = []
    
    saveFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_peaks"
    
    
    for i in range(len(li)):
        #first input 
        if (i-1<0):
            if (li[i+1] < li[i]):
                peaks.append((li[i],(i*0.0232)))
        #last input
        if ((i+1)==len(li)):
            if (li[i-1] < li[i]):
                peaks.append((li[i],(i*0.0232)))
        #middle inputs
        if ((i-1>0) and ((i+1)!=len(li)) and (li[i-1] < li[i]) and (li[i+1] < li[i])):
            peaks.append((li[i],(i*0.0232)))
            
    np.save(saveFile, peaks)
    

def threshold(unit, start_time, thresh):
    if (start_time == 0):
        end_time = 605
    else:
        end_time = start_time+610
        
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_peaks.npy"
    threshold_peaks = []
    predicted = []
    groundValues = []
    for i in np.load(checkFile):
        if (i[0]>=thresh):
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

    return F,P,R


"""
Calling 

unit = 1
start_time = 38340
fmin_input = 1500
h_length = 256

onset(unit, start_time,fmin_input,h_length)
peak_picking(unit, start_time)
  
thresh_vals = []
x = 0
while (x<1):
    thresh_vals.append(x)
    x += 0.01


precision = []
recall = []
for i in thresh_vals:
    print("Threshold is: "+str(i))
    F, P, R = threshold(1,38340,i)
    print("Precision is: "+str(P))
    print("Recall is: "+str(R))
    print('***************************')
    precision.append(P)
    recall.append(R)
    
plt.plot(recall,precision)
plt.ylabel('Precision')
plt.xlabel('Recall')
plt.show() 


u = 1
s = 240
e = 300
fmin = 1500
thresh = 1

retrieve(u, s, e)
onset(u, s, e, fmin,(e-s))
peak_picking(u, s, e)
threshold(u, s, e, thresh)
eval_score(u, s, e)
"""




