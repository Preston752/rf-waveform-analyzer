import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

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

# Add this after generating your BPSK signal
SNR_dB = 10  # Signal-to-Noise Ratio in dB
signal_power = np.mean(bpsk_signal**2)
noise_power = signal_power / (10**(SNR_dB/10))
noise = np.sqrt(noise_power) * np.random.randn(len(bpsk_signal))
noisy_signal = bpsk_signal + noise

# Design a lowpass filter
# We want to keep frequencies around our carrier (100 kHz) 
# but reject high-frequency noise
nyquist = fs / 2
cutoff = 150e3  # 150 kHz cutoff frequency
normal_cutoff = cutoff / nyquist

# Create Butterworth filter
b, a = signal.butter(5, normal_cutoff, btype='low')

# Apply filter to noisy signal
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# Plot comparison
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.plot(t[:2000], noisy_signal[:2000])
ax1.set_title(f'Noisy BPSK Signal (SNR = {SNR_dB} dB)')
ax1.set_ylabel('Amplitude')
ax1.grid(True)

ax2.plot(t[:2000], filtered_signal[:2000])
ax2.set_title('After Lowpass Filtering')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Amplitude')
ax2.grid(True)

plt.tight_layout()
plt.show()