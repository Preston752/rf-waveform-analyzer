import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 10e6  # 10 MHz sampling rate
pulse_duration = 100e-6  # 100 microseconds
t_pulse = np.arange(0, pulse_duration, 1/fs)

# Chirp parameters
f_start = 1e6
f_stop = 5e6

# Generate transmitted chirp
chirp_rate = (f_stop - f_start) / pulse_duration
phase = 2 * np.pi * (f_start * t_pulse + 0.5 * chirp_rate * t_pulse**2)
transmitted_chirp = np.sin(phase)

# Simulate received signal (same chirp, but we'll add delay for target)
# For now, just use the same chirp as if target is at range = 0
received_signal = transmitted_chirp.copy()

# MATCHED FILTER - correlate received signal with transmitted chirp
# This is the KEY step in pulse compression
matched_filter_output = np.correlate(received_signal, transmitted_chirp, mode='same')

# Time axis for plotting
t_output = np.arange(len(matched_filter_output)) / fs

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

# Plot 1: Transmitted chirp
ax1.plot(t_pulse * 1e6, transmitted_chirp)
ax1.set_title('Transmitted Chirp (100 μs long)')
ax1.set_xlabel('Time (μs)')
ax1.set_ylabel('Amplitude')
ax1.grid(True)

# Plot 2: Received signal (same as transmitted for now)
ax2.plot(t_pulse * 1e6, received_signal)
ax2.set_title('Received Signal')
ax2.set_xlabel('Time (μs)')
ax2.set_ylabel('Amplitude')
ax2.grid(True)

# Plot 3: Matched filter output (COMPRESSED PULSE!)
ax3.plot(t_output * 1e6, np.abs(matched_filter_output))
ax3.set_title('Matched Filter Output - COMPRESSED PULSE!')
ax3.set_xlabel('Time (μs)')
ax3.set_ylabel('Amplitude')
ax3.grid(True)
ax3.set_xlim([40, 60])  # Zoom in to see the spike

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 10e6
pulse_duration = 100e-6
t_pulse = np.arange(0, pulse_duration, 1/fs)

# Chirp parameters
f_start = 1e6
f_stop = 5e6

# Generate transmitted chirp
chirp_rate = (f_stop - f_start) / pulse_duration
phase = 2 * np.pi * (f_start * t_pulse + 0.5 * chirp_rate * t_pulse**2)
transmitted_chirp = np.sin(phase)

# SIMULATE MULTIPLE TARGETS
c = 3e8
target_ranges = [8e3, 15e3, 22e3]  # 8 km, 15 km, 22 km
target_amplitudes = [0.7, 0.5, 0.3]  # Different reflectivities

# Find max delay needed
max_delay = int(2 * max(target_ranges) / c * fs)
total_samples = len(transmitted_chirp) + max_delay + 100
received_signal = np.zeros(total_samples)

# Add each target's echo
for target_range, amplitude in zip(target_ranges, target_amplitudes):
    delay_samples = int(2 * target_range / c * fs)
    received_signal[delay_samples:delay_samples + len(transmitted_chirp)] += transmitted_chirp * amplitude

# Matched filter
matched_filter_output = np.correlate(received_signal, transmitted_chirp, mode='full')
t_output = (np.arange(len(matched_filter_output)) - len(transmitted_chirp) + 1) / fs
range_output = (t_output * c) / 2

# Plot
plt.figure(figsize=(14, 6))
plt.plot(range_output / 1000, np.abs(matched_filter_output))
plt.title('Pulse Compression - Multiple Targets Detected')
plt.xlabel('Range (km)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim([0, 30])

# Mark expected targets
for target_range in target_ranges:
    plt.axvline(x=target_range/1000, color='r', linestyle='--', alpha=0.5)

plt.legend([f'Targets at: {[r/1000 for r in target_ranges]} km'])
plt.tight_layout()
plt.show()