
# coding: utf-8

# In[16]:


import numpy as np
import Paths as p


# In[27]:


def threshold(unit, start_time, end_time, thresh):
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_peaks.npy"
    threshold_peaks = []
    for i in np.load(checkFile):
        if (i>thresh):
            threshold_peaks.append(i)
            
    saveFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_thresh_peaks.npy"
    np.save(saveFile, threshold_peaks)


# In[28]:


threshold(1,38340,38400,1)


# In[ ]:




