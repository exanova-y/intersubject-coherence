import mne
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import coherence

# filter data
# display the power spectra
# recognize ERPs
# resting data

def load_eeg_data(filename):
  path_string = 'eeg_recordings\\'+filename
  print(path_string)
  raw = mne.io.read_raw_edf(path_string) 
  return raw

def graph_update(fn): # for each frame number. fn starts from 0 and goes up to include 100
   pass
#   #Update data (considering a moving window effect here) with points
#   x, y1, y2 = freqs_yoyo[fn], psds_laila[fn], psds_yoyo[fn]

#   #Update line data
#   # each frame's data refers to the entire dataset for each line
#   line1.set_xdata(x)
#   line1.set_ydata(y1)
#   line2.set_xdata(x)
#   line2.set_ydata(y2)
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
  #print("psd yoyo", psd_yoyo)
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




# iniialize the graph

# # we use ax.plot, an object oriented plot
# # explicit plotting to axes if you want to add more axes


# ------
# num_points = 100
# num_frames = 120
# #x = np.linspace(0, 100, num_points)
# x = freqs_yoyo
# y1 = psds_laila[0] # get rid of the extra bracket dimension
# y2 = psds_yoyo[0]
# print(x, y1, y2)

# fig, ax = plt.subplots()
# line1, = ax.plot(x, y1, label='Laila', color='blue')
# line2, = ax.plot(x, y2, label='Yoyo', color='orange')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_xlim(0, 105)
# ax.set_ylim(-5, 5)  # Set appropriate y-axis limits
# ax.legend()
# -----


#animation = FuncAnimation(fig, graph_update, frames=100, blit=True)
#plt.show()

# isc_per_second = []  # List to store ISC values for each second
# for i in range(len(psds_yoyo)):
#     yoyo_psd = psds_yoyo[i]  # Access PSDs for current snapshot
#     laila_psd = psds_laila[i]
#     isc_values = []  # List to store ISC for each frequency bin

#     # Calculate ISC for each frequency bin
#     for freq_bin in range(yoyo_psd.shape[1]):
#         coherence_val = coherence(yoyo_psd[freq_bin], laila_psd[freq_bin])
#         isc_values.append(abs(coherence_val[0]))  # Absolute value of coherence

#     # Optional: Average ISC across frequencies
#     avg_isc = np.mean(isc_values)

#     # Store ISC value (per frequency bin or averaged)
#     isc_per_second.append(avg_isc)  # You can replace with isc_values for per-bin data

#from scipy.signal import coherence
# Assuming psds_yoyo and psds_laila are your PSD arrays (shape: [n_windows, n_frequencies])

# Access PSDs for the first second (assuming 0-based indexing)
yoyo_psd = psds_yoyo
laila_psd = psds_laila

isc_values = []  # List to store ISC for each frequency bin

# Calculate ISC for each frequency bin
print(range(yoyo_psd.shape[1]))
for freq_bin in range(yoyo_psd.shape[1]):
    coherence_val = coherence(yoyo_psd[freq_bin], laila_psd[freq_bin])
    isc_values.append(abs(coherence_val[0]))  # Absolute value of coherence

# Optional: Average ISC across frequencies
avg_isc = np.mean(isc_values)

# Print ISC results
print("ISC for the first second (per frequency bin):")
print(isc_values)

if avg_isc:  # Check if averaging was performed
  print("ISC for the first second (averaged):", avg_isc)
