import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 10e6  # 10 MHz sampling rate (higher for radar)
duration = 10e-6  # 10 microseconds
t = np.arange(0, duration, 1/fs)

# Chirp parameters
f_start = 1e6  # Start at 1 MHz
f_stop = 5e6   # End at 5 MHz (sweeps across 4 MHz bandwidth)

# Generate LFM chirp
# Frequency sweeps linearly from f_start to f_stop
chirp_rate = (f_stop - f_start) / duration
instantaneous_freq = f_start + chirp_rate * t
phase = 2 * np.pi * (f_start * t + 0.5 * chirp_rate * t**2)
chirp_signal = np.sin(phase)

# Plot the chirp in time domain
plt.figure(figsize=(12, 4))
plt.plot(t * 1e6, chirp_signal)  # Convert to microseconds
plt.xlabel('Time (μs)')
plt.ylabel('Amplitude')
plt.title('Linear FM Chirp (1-5 MHz over 10 μs)')
plt.grid(True)
plt.show()