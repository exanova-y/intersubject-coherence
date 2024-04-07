import mne
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# filter data
# display the power spectra
# recognize ERPs
# resting data

def load_eeg_data(filename):
  path_string = 'eeg_recordings\\'+filename
  print(path_string)
  raw = mne.io.read_raw_edf(path_string) 
  return raw


def graph_init():
  # we use ax.plot, an object oriented plot
  # explicit plotting to axes if you want to add more axes
  num_points = 100
  #x = np.linspace(0, 100, num_points)
  x = freqs_yoyo
  y1 = psds_laila
  y2 = psds_yoyo
  fig, ax = plt.subplots()
  line1, = ax.plot(x, y1, label='Laila', color='blue')
  line2, = ax.plot(x, y2, label='Yoyo', color='orange')
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_ylim(-1.2, 1.2)  # Set appropriate y-axis limits
  ax.legend()

def update(fn): # for each frame number. fn starts from 0.
  pass
  # Update data (considering a moving window effect here)
  #x, y1, y2 = freqs_yoyo[fn], psds_laila[fn], psds_yoyo[fn]

  # Update line data
#   line1.set_xdata(x_data)
#   line1.set_ydata(y1_data)
#   line2.set_xdata(x_data)
#   line2.set_ydata(y2_data)
#   return line1, line2


# Load EEG data for both participants
yoyo_round_1 = load_eeg_data('yoyo_round_1.edf')
laila_round_1 = load_eeg_data('laila_round_1.edf')

# Sample rate (Hz) - Replace with actual sampling rate
fs = 256
duration = 60 # in seconds
window_len = 1
step_size = 0.5

time_points = [] # shared array

psds_yoyo = [] # y axis points
psds_laila = []
freqs_yoyo = [] # x axis points
freqs_laila = []

for t in range(0, duration, int(step_size*fs)): # loop through 60 seconds for the total number of steps
  # extract data for current window
  data_window_yoyo = yoyo_round_1.get_data(start=t, stop=t+window_len) # starting and end time point
  # data window yoyo is an 8 x 1 array containing microvolt data from the 8 eeg channels from neurosity
  # need to transpose into (n times, n channels)
  data_window_laila = laila_round_1.get_data(start=t, stop=t+window_len)
  data_window_yoyo = data_window_yoyo.T 
  data_window_laila = data_window_laila.T 
  # compute PSD using Welch's method
  psd_yoyo, freq_yoyo = mne.time_frequency.psd_array_welch(x=data_window_yoyo, sfreq=fs, fmin=0, fmax=100, n_per_seg = 512) # n per sec is the same as sampling rate
  psd_laila, freq_laila = mne.time_frequency.psd_array_welch(x=data_window_laila, sfreq=fs, fmin=0, fmax=100, n_per_seg = 512)
  print("psd yoyo", psd_yoyo)
  # store results

  # time points are shared
  time_points.append(t / fs)

  # psds
  psds_yoyo.append(psd_yoyo)
  psds_laila.append(psd_laila)

  # freqs
  freqs_yoyo.append(freq_yoyo)
  freqs_laila.append(freq_laila)
  #print("finished window")
# output isc score

#print(psds_laila)
#print(psds_yoyo)
graph_init()