
# coding: utf-8

# In[2]:


import numpy as np
import Paths as p
#checkFile = p.get_data() + "blank.npy"


# In[16]:


def peak_picking(unit, start_time, end_time):      #checkFile):
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_detections.npy"
    li = np.load(checkFile) #[100,50,30,45,25,60,12,100,90,80,300]
    peaks = []
    
    saveFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_peaks"
    
    
    for i in range(len(li)):
        #first input 
        if (i-1<0):
            if (li[i+1] < li[i]):
                #print(li[i],i)
                peaks.append((li[i],i))
        #last input
        if ((i+1)==len(li)):
            if (li[i-1] < li[i]):
                peaks.append((li[i],i))
                #print(li[i],i)
        #middle inputs
        if ((i-1>0) and ((i+1)!=len(li)) and (li[i-1] < li[i]) and (li[i+1] < li[i])):
            peaks.append((li[i],i))
            #print(li[i],i)
            
    np.save(saveFile, peaks)
    #np.load(checkFile)
    #print("li size: "+ str(np.size(li)))
    #print("peaks size: " + str(len(peaks)))


# In[17]:


peak_picking(1,38340,38400)


# In[8]:


np.load(p.get_data() + "01_S_38340_E_38400_peaks.npy")


# In[15]:





# In[ ]:




