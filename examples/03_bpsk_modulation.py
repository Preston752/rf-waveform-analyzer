import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1e6  # Sampling frequency (1 MHz)
f_carrier = 100e3  # Carrier frequency (100 kHz)
duration = 0.001  # 1 millisecond
t = np.arange(0, duration, 1/fs)  # Time vector

# Digital data to transmit (random bits)
bit_rate = 10e3  # 10 kbps
bits_per_second = int(bit_rate)
num_bits = int(duration * bits_per_second)
data_bits = np.random.randint(0, 2, num_bits)

# Create BPSK signal (0 = phase 0, 1 = phase π)
samples_per_bit = int(fs / bit_rate)
bpsk_signal = np.zeros(len(t))

for i, bit in enumerate(data_bits):
    start = i * samples_per_bit
    end = start + samples_per_bit
    if end > len(t):
        end = len(t)
    
    if bit == 0:
        bpsk_signal[start:end] = np.sin(2 * np.pi * f_carrier * t[start:end])
    else:
        bpsk_signal[start:end] = -np.sin(2 * np.pi * f_carrier * t[start:end])

# Plot
plt.figure(figsize=(12, 4))
plt.plot(t[:5000], bpsk_signal[:5000])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('BPSK Modulated Signal')
plt.grid(True)
plt.show()