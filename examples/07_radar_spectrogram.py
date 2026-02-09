import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 10e6  # 10 MHz sampling rate
duration = 100e-6  # 100 microseconds
t = np.arange(0, duration, 1/fs)

# Chirp parameters
f_start = 1e6
f_stop = 5e6

# Generate LFM chirp
chirp_rate = (f_stop - f_start) / duration
phase = 2 * np.pi * (f_start * t + 0.5 * chirp_rate * t**2)
chirp_signal = np.sin(phase)

# Spectrogram
plt.figure(figsize=(12, 6))
spectrum, freqs, time_bins, im = plt.specgram(chirp_signal, Fs=fs, NFFT=256, noverlap=250, cmap='viridis')

plt.ylabel('Frequency (MHz)')
plt.xlabel('Time (μs)')
plt.title('Spectrogram - Shows Frequency Sweep Over Time')
plt.colorbar(im, label='Intensity (dB)')

# Fix axis labels - 6 labels for 6 tick positions
plt.yticks(np.arange(0, 6e6, 1e6), ['0', '1', '2', '3', '4', '5'])
time_ticks = np.arange(0, duration, 20e-6)
plt.xticks(time_ticks, [f'{t*1e6:.0f}' for t in time_ticks])

plt.ylim([0, 6e6])
plt.show()