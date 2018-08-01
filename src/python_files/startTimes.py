import os

import HPC_Paths as p

def get_start_time(unit):
    start_times = []
    unit = str(unit).zfill(2)
    for file in os.listdir(p.get_trimmed_annotation(unit)):
        if (file.startswith(unit) and file.endswith(".txt")):
            file_name = file
            file_name = file_name[5:]
            file_name = file_name.partition("_E_")
            start_times.append(file_name[0])
    
    return start_times
