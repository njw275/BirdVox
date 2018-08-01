
# coding: utf-8

# In[ ]:


def get_unit_recordings():
    return "/scratch/njw275/full_night_recordings/unit"

def get_unit_annotations():
    return "/scratch/njw275/annotations/unit"

def get_trimmed_audio(unit):
    return "/scratch/njw275/trimmed_recordings/unit" + str(unit).zfill(2) + "/unit"

def get_data():
    return "/scratch/njw275/"

def get_detections(unit):
    return "/scratch/njw275/detections/05_medianfilt/unit" + str(unit).zfill(2) + "/unit"

def get_peaks(unit):
    return "/scratch/njw275/peaks/05_medianfilt/unit" + str(unit).zfill(2) + "/"

def get_trimmed_annotation(unit):
    return "/scratch/njw275/trimmed_annotations/unit" + str(unit).zfill(2) + "/"

def get_filtered_detections(unit):
    return "/scratch/njw275/detections/05_medianfilt/filtered/unit" + str(unit).zfill(2) + "/unit"
