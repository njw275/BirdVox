
# coding: utf-8

# In[9]:


import sox
import os
import pandas as pd


# In[22]:


#given a unit number, a start time, and an end time, retrieves the audio signal and the corresponding ground truth.
def retrieve (unit, start_time, end_time):
    #input audio signal
    input_audio = "/Users/nicholaswhite/data/full_night_recordings/unit" + str(unit).zfill(2) + ".flac"
    #where to save the trimmed audio file
    output_audio = "/Users/nicholaswhite/data/Trimmed_Recordings/unit" + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".flac"
    
    annotations_dir = '/Users/nicholaswhite/data/annotations'
    #Find the correct unit and read it 
    annotation_path = os.path.join(annotations_dir, "unit" + str(unit).zfill(2) + ".txt")
    annotation = pd.read_csv(annotation_path, sep="\t")
    
    #Find the ground truth between the start and end times
    for i in annotation["Begin Time (s)"]:
        if ((i >= start_time) and (i <= end_time)):
            print(i)
    
    #trim the audio from start to end times and save it where output_audio specified
    tfm = sox.Transformer()
    tfm.trim(start_time, end_time)
    tfm.build(input_audio,output_audio)


# In[23]:


retrieve(1,0,61.476)


# In[ ]:




