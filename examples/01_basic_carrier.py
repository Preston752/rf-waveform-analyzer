import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1e6  # Sampling frequency (1 MHz)
f_carrier = 100e3  # Carrier frequency (100 kHz)
duration = 0.001  # 1 millisecond
t = np.arange(0, duration, 1/fs)  # Time vector

# Generate a simple sine wave (carrier signal)
signal = np.sin(2 * np.pi * f_carrier * t)

# Plot it
plt.figure(figsize=(12, 4))
plt.plot(t[:1000], signal[:1000])  # Plot first 1000 samples
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Simple RF Carrier Signal (100 kHz)')
plt.grid(True)
plt.show()