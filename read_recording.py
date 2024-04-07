import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mne

# filter data
# display the power spectra
# recognize ERPs
# resting data

def load_eeg_data(path_string):
  raw = mne.io.read_raw_edf(path_string) 
  return raw

# Load EEG data for both participants
yoyo_round_1 = load_eeg_data('yoyo_round_1.edf')
laila_round_1 = load_eeg_data('laila_round_1.edf')

# Sample rate (Hz) - Replace with actual sampling rate
sfreq = 256
duration = 60 # in seconds
window_len = 1
step_size = 0.5

time_points = [] # shared array

psds_yoyo = [] # y axis points
psds_laila = []
freqs_yoyo = [] # x axis points
freqs_laila = []

for t in range(0, duration, int(step_size*sfreq)): # loop through 60 seconds for the total number of steps
  # extract data for current window
  data_window_yoyo = yoyo_round_1.get_data(t=t, tmax=t+window_len)
  data_window_laila = laila_round_1.raw.get_data(t=t, tmax=t+window_len)

  # compute PSD using Welch's method
  psd_yoyo, freq_yoyo = mne.time_frequency.psd_array_welch(window_len, sfreq) # window len of 
  psd_laila, freq_laila = mne.time_frequency.psd_array_welch(window_len, sfreq)

  # store results

  # time points are shared
  time_points.append(t / sfreq)

  # psds
  psds_yoyo.append(psd_yoyo)
  psds_laila.append(psd_laila)

  # freqs
  freqs_yoyo.append(freq_yoyo)
  freqs_laila.append(freq_laila)


# Plot power spectra
plt.figure(figsize=(10, 6))

plt.plot(f1, Pxx1, label='Participant 1')
plt.plot(f2, Pxx2, label='Participant 2')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (uV^2/Hz)')
plt.title('Power Spectra of EEG Data (Participants 1 & 2)')
plt.legend()
plt.grid(True)

plt.show()
