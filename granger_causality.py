import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import mne
from time import sleep

### imports


# import data
def load_eeg_data(filename):
  path_string = 'eeg_recordings\\'+filename
  print(path_string)
  raw = mne.io.read_raw_edf(path_string) 
  return raw

# Load EEG data for both participants
yoyo_r1 = load_eeg_data('yoyo_round_1.edf')
laila_r1 = load_eeg_data('laila_round_1.edf')
yoyo_r1_desc = yoyo_r1.info
print(yoyo_r1_desc) 
# note that there is a low pass of 128 Hz, meaning frequencies > 128 Hz will be reduced!

# visualize data 
yoyo_r1.compute_psd(fmax=128).plot(picks="data", exclude="bads", amplitude=False)
yoyo_r1.plot(duration=5, n_channels=8)
plt.show() # to make the graph appear on the screen until you manually close it 
# window size = 8 seconds

### preprocessing

# filtering
# downsampling
# 8*256*32 = 65536 kb per second

# preprocess the data with mne - need to filter ADHD signals!

# visualize it again 


# conduct adf test and differencing if needed for being stationary
# for each channel pair conduct adf test

# use granger causality