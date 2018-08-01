
# coding: utf-8

# In[23]:


import numpy as np
import os
import pandas as pd
import random

#tSave = pd.read_csv("testSaving.txt", sep="\t")
#startTimes = tSave['Begin Time (s)']

annotations_dir = '/Users/nicholaswhite/data/annotations'
unit = 1
annotation_path = os.path.join(annotations_dir, "unit" + str(unit).zfill(2) + ".txt")
annotation = pd.read_csv(annotation_path, sep="\t")

match = False
changedValues = pd.read_csv("/Users/nicholaswhite/Desktop/changedValues.txt",sep="\t")["Changed Values"]
realValues = annotation['Begin Time (s)']
for i in realValues:
    match = False
    for z in changedValues:
        #print("Following Real value is (i): "+ str(i))
        if (((i-z)>= 0) and (i-z) < 0.05) or (((z-i)>= 0) and (z-i) < 0.05):
            print("Correct Prediction -> Predicted: " + str('{0:.3f}'.format(z)) + " (s) | True Time: " + str('{0:.3f}'.format(i)) + " (s)")
            match = True
    if (not(match)): 
        print("Real (" + str('{0:.3f}'.format(i)) + ") has no predicted match")
        match = False

print("**********************************************************************")
print("**********************************************************************")
print("**********************************************************************")
print("**********************************************************************")
print("**********************************************************************")

pred = False
for z in changedValues:
    pred = False
    for i in realValues:
        if (((i-z)>= 0) and (i-z) < 0.05) or (((z-i)>= 0) and (z-i) < 0.05):
            pred = True
    if (not(pred)):
        print("Predicted Guess (" + str('{0:.3f}'.format(z)) + ") has no true match")
        pred = False


# In[ ]:




