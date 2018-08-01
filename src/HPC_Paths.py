#Paths file for navigating hpc
import os

def get_unit_recordings():
    return os.path.join(get_data(), "full_night_recordings", "unit")

def get_unit_annotations():
    return os.path.join(get_data(), "annotations", "unit")

def get_trimmed_audio(unit):
    return os.path.join(get_data(), "trimmed_recordings",
        "unit" + str(unit).zfill(2), "unit")

def get_data():
    return "/scratch/njw275"
