import sox
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import HPC_Paths as p
import startTimes as st

print("hi")
#given a unit number, a start time, and an end time, retrieves the audio signal and the corresponding ground truth.
def retrieve (unit, start_time):
   
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

   annotation_path = os.path.join(p.get_unit_annotations() + str(unit).zfill(2) + ".txt")
   annotation = pd.read_csv(annotation_path, sep="\t")
    
   #Find the ground truth between the start and end times
   for i in annotation["Begin Time (s)"]:
       if ((i >= start_time) and (i <= end_time)):
           print(i)
           with open(p.get_trimmed_annotation(unit) + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".txt", "w") as text_file:
               text_file.write(str(i)+"\n")


import soundfile as sf
#1,2,3,5,7,10
fname = '/scratch/njw275/full_night_recordings/unit10.flac'
f = sf.SoundFile(fname)
time_in_seconds = (len(f) / f.samplerate)

start = 0 
x = 1
unit = 10

while(x):
    if (start == 0):
        end = 605
        retrieve(unit,start)
        start = (end-10)
    else:
        end = start+610
        retrieve(unit,start)
        start = (end-10)
    if (start > time_in_seconds):
        x = 0
        break

