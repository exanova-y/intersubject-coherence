import numpy as np
import matplotlib.pyplot as plt
import mne

#raw = mne.io.read_raw_fif('yoyo_resting.edf')  # Replace with your filename
# filter data

# resting data

# display the power spectra

# recognize ERPs
# Replace with your EEG data loading function
def load_eeg_data(path_string):
  raw = mne.io.read_raw_edf(path_string) 
  return raw

# Load EEG data for both participants
yoyo_round_1 = load_eeg_data('yoyo_round_1.edf')
laila_data = load_eeg_data('laila_round_1.edf')

# Sample rate (Hz) - Replace with actual sampling rate
fs = 256

# Compute power spectrum using Welch's method
def compute_power_spectrum(data, fs):
  from scipy.signal import welch
  f, Pxx = welch(data, fs, nperseg=1024)
  return f, Pxx

# Calculate power spectra for both participants
f1, Pxx1 = compute_power_spectrum(participant1_data, fs)
f2, Pxx2 = compute_power_spectrum(participant2_data, fs)

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
