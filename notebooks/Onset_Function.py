
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import Paths as p


# In[24]:


# First, load some audio and plot the spectrogram

#a = "/Users/nicholaswhite/data/Trimmed_Recordings/unit01_S_0_E_60.wav"

#
#
#rength(y=y, sr=sr,aggregate=np.median,fmax=8000, n_mels=256)
#
def onset(unit, start_time,end_time,fmin_input):
    file = p.get_trimmed_audio() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + ".wav"

    y, sr = librosa.load(file, duration=60.0)
    #"/Users/nicholaswhite/Desktop/test_audio.wav", duration=10.0)
    D = librosa.stft(y)
    times = librosa.frames_to_time(np.arange(D.shape[1]))
    plt.figure()
    ax1 = plt.subplot(2, 1, 1)
    #librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
    #                         y_axis='log', x_axis='time',fmin=fmin)
    S = librosa.feature.melspectrogram(y, sr=sr,fmin=fmin_input)
    librosa.display.specshow(librosa.power_to_db(S,
                                                 ref=np.max),
                             y_axis='mel', fmax=8000,
                             x_axis='time')
    plt.title('Power spectrogram')

    # Construct a standard onset function

    onset_env = librosa.onset.onset_strength(y=y, sr=sr,fmin=fmin_input)    #,fmin=1000)
    plt.subplot(2, 1, 2, sharex=ax1)
    plt.plot(times, 2 + onset_env / onset_env.max(), alpha=0.8,
             label='Mean (mel)')

    saveFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_onsets"
    checkFile = p.get_data() + str(unit).zfill(2) + "_S_" + str(start_time) + "_E_" + str(end_time) + "_onsets.npy"
    np.save(saveFile, onset_env)
    # Median aggregation, and custom mel options

    #onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                             #aggregate=np.median,
                                             #fmax=8000, n_mels=256)
    #plt.plot(times, 1 + onset_env / onset_env.max(), alpha=0.8,
             #label='Median (custom mel)')

    # Constant-Q spectrogram instead of Mel

    #onset_env = librosa.onset.onset_strength(y=y, sr=sr,
    #                                         feature=librosa.cqt)
    #plt.plot(times, onset_env / onset_env.max(), alpha=0.8,
    #         label='Mean (CQT)')

    plt.legend(frameon=True, framealpha=0.75)
    plt.ylabel('Normalized strength')
    plt.yticks([])
    plt.axis('tight')
    plt.tight_layout()
    plt.show()

    #Then call the onset_strength function in the librosa module 
    #to obtain the SuperFlux detection function for the audio signal.
    #https://librosa.github.io/librosa/_modules/librosa/onset.html


# In[25]:


onset(1,38340,38400,1500) 


# In[ ]:




