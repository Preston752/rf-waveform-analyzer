import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1e6  # Sampling frequency (1 MHz)
f_carrier = 100e3  # Carrier frequency (100 kHz)
duration = 0.001  # 1 millisecond
t = np.arange(0, duration, 1/fs)  # Time vector

# Generate a simple sine wave (carrier signal)
signal = np.sin(2 * np.pi * f_carrier * t)

# Compute FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), 1/fs)

# Plot spectrum
plt.figure(figsize=(12, 4))
plt.plot(frequencies[:len(frequencies)//2], 
         np.abs(fft_result[:len(fft_result)//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.grid(True)
plt.show()