import HPC_Paths as p
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mir_eval
import librosa
import os
import sox
from mir_eval import util

def onset(unit, start_time,fmin_input,h_length, feature_input):
    start_time = int(start_time)
    if (start_time == 0):
        end_time = 605
    #last start_time for units 1,2,3,5,7
    elif (start_time == 38995):
        if (unit == 1):
            end_time = 39285 
        elif (unit == 2):
            end_time = 39301 
        elif (unit == 3):
            end_time = 39355 
        elif (unit == 5):
            end_time = 39356 
        elif (unit == 7):
            end_time = 39295 
    #last start_time for unit 10
    elif (start_time == 29395 and unit == 10):
        end_time = 29483 
    else:
        end_time = start_time+610
        
    duration_length = end_time - start_time
    
    file = p.get_trimmed_audio(unit) + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".wav"

    y, sr = librosa.load(file, duration=duration_length)
    
    if feature_input == librosa.stft:
        S = feature_input(y, hop_length=h_length, n_fft=2*h_length)
    elif feature_input == librosa.feature.melspectrogram:
        S = feature_input(y, sr=sr, hop_length=h_length, fmin=fmin_input)
        S = librosa.logamplitude(S, ref=1.0)

    #onset_env = librosa.onset.onset_strength(S=S, aggregate = np.median)
    onset_env = librosa.onset.onset_strength(S=S)
    saveFile = p.get_detections(unit) + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_detections"
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_detections.npy"
    np.save(saveFile, onset_env)
    

def peak_picking(unit, start_time, hop_duration): #medfilt_size=None):
    start_time = int(start_time)
    if (start_time == 0):
        end_time = 605
    #last start_time for units 1,2,3,5,7
    elif (start_time == 38995):
        if (unit == 1):
            end_time = 39285 
        elif (unit == 2):
            end_time = 39301 
        elif (unit == 3):
            end_time = 39355 
        elif (unit == 5):
            end_time = 39356 
        elif (unit == 7):
            end_time = 39295 
    #last start_time for unit 10
    elif (start_time == 29395 and unit == 10):
        end_time = 29483 
    else:
        end_time = start_time+610
        
    checkFile = p.get_detections(unit) + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_detections.npy"
    li = np.load(checkFile)
    #if medfilt_size is not None:
	#pass # remove me
	# apply scipy.signal.medfilt
    peaks = []
    
    saveFile = p.get_peaks(unit) + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_peaks"
    
    
    for i in range(len(li)):
        #first input 
        if (i-1<0):
            if (li[i+1] < li[i]):
                #print(li[i],i)
                peaks.append((li[i],(i*hop_duration)))
        #last input
        if ((i+1)==len(li)):
            if (li[i-1] < li[i]):
                peaks.append((li[i],(i*hop_duration)))
                #print(li[i],i)
        #middle inputs
        if ((i-1>0) and ((i+1)!=len(li)) and (li[i-1] < li[i]) and (li[i+1] < li[i])):
            peaks.append((li[i],(i*hop_duration)))
            #print(li[i],i)
            
    np.save(saveFile, peaks)

def threshold(unit, start_time, thresh):
    start_time = int(start_time)
    if (start_time == 0):
        end_time = 605
    #last start_time for units 1,2,3,5,7
    elif (start_time == 38995):
        if (unit == 1):
            end_time = 39285 
        elif (unit == 2):
            end_time = 39301 
        elif (unit == 3):
            end_time = 39355 
        elif (unit == 5):
            end_time = 39356 
        elif (unit == 7):
            end_time = 39295 
    #last start_time for unit 10
    elif (start_time == 29395 and unit == 10):
        end_time = 29483 
    else:
        end_time = start_time+610
    
    checkFile = p.get_peaks(unit) + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_peaks.npy"
    threshold_peaks = []
    predicted = []
    groundValues = []
    for i in np.load(checkFile):
        #print(i)
        if (i[0]>=thresh):
            threshold_peaks.append(i)
            predicted.append(i[1]) #+38340)
    
    truth = p.get_trimmed_annotation(unit) + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".txt"

    for line in open(truth,'r'):
        line = line.strip('\n')
        line = float(line) #- 38340
        groundValues.append(line)
    
    groundValues = np.array(groundValues)
    predicted = np.array(predicted)
    
    
    
    #F, P, R = mir_eval.onset.f_measure(groundValues,predicted) #(reference_onsets, estimated_onsets)

    
    Tp = float(len(util.match_events(groundValues, predicted,0.05)))
    Fp = float(len(predicted)) - float(len(util.match_events(groundValues, predicted,0.05)))
    Fn = float(len(groundValues)) - float(len(util.match_events(groundValues, predicted,0.05)))


    return Tp, Fp, Fn #F, P, R



