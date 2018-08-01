import countingOnsets as co
import medianfilt_DetectionEvalSourceCode as det
import HPC_Paths as p
import startTimes as st
import librosa
import scipy.signal as sci
import numpy as np
from joblib import Parallel, delayed

#for split_id:
fmin_input = 2000
h_length = 256
sr = 22050
h_duration = h_length / sr
units = [1,2,3,5,7,10]
k_size = 5
feature = librosa.stft

def createOnsetsAndPeaks(unit):
    saveFile = "/scratch/njw275/detections/05_medianfilt/filtered/unit" + str(unit).zfill(2)
    print("Unit " + str(unit).zfill(2))
    # TODO: read the available unit files -> start_times
    start_times = st.get_start_time(unit)
    #start_times = [0]
    #for start_time in start_times:
        # Create onset detection function (writes to a file)
        #print(start_time)
        #det.onset(unit, start_time, fmin_input, h_length,feature)
        # Peak picks (read from file above, write to a new file)
    for start_time in start_times:
        #detections = p.get_detections(unit)
        check = "/scratch/njw275/detections/05_medianfilt/unit01/unit01_S_0_E_605_detections.npy"
        detections = np.load(check)
        detections = detections.astype(float)
        filt_detections = sci.medfilt(detections, kernel_size=5)
        filt_detections = np.array(filt_detections)
        saveFile = p.get_filtered_detections(unit)
        np.save(saveFile, filt_detections)
        #det.peak_picking(unit, start_time, h_duration)

Parallel(n_jobs=-1)(delayed(createOnsetsAndPeaks)(unit) for unit in units)
