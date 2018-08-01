
# coding: utf-8

# In[13]:


import HPC_Paths as p

def counting_onsets(unit, start_time):
    count = 0
    
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

    with open(p.get_trimmed_annotation(unit) + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".txt", "r") as text_file:
        for i in text_file:
            count+=1

    return count


# In[ ]:




