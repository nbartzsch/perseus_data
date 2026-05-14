import os

import matplotlib.pyplot as plt
import numpy as np

# Load sensor data from CSV file
data_file = "Perseus/kistler_data/Medusa_02/deflagration/firing_01/Medusa_02_deflagration_01_complete.csv"
data_1 = np.genfromtxt(data_file, delimiter=",")

# Get the directory path of the input file
output_dir = os.path.dirname(data_file)

# Extract time and sensor values
time = data_1[1:, 0]
sensor_values_1 = data_1[1:, 2]
# sensor_values_2 = data_1[1:, 2]

# Shift all time values down by the lowest value in the column
time = time - np.min(time)
max_time = np.max(time)

# Calculate baseline (average of first 100 values)
baseline = np.mean(sensor_values_1[:100])

# Shift all values by subtracting the baseline
sensor_values_1 = sensor_values_1 - baseline

print("Data loaded")
print("Max time:", max_time)

# # Plot time vs sensor_values_1
# plt.figure()
# plt.plot(time, sensor_values_1, label='Complete Sensor Response of Sensor 02')
# plt.xlabel('Time (s)')
# plt.ylabel('Sensor Response')
# plt.title('Complete Sensor Response of Sensor 02')
# plt.grid(True)
# plt.xlim(0, 1.2)
# plt.ylim(-290, 70)
# plt.savefig(os.path.join(output_dir, 'response_time_02.svg'))
# #plt.show()

# Parameters
interval = 0.01  # seconds
sampling_rate = 1 / (time[1] - time[0])
n_intervals = int((time[-1] - time[0]) // interval)

# Prepare the time and frequency axes
time_axis = np.arange(n_intervals) * interval
freq_axis = np.fft.fftfreq(int(interval * sampling_rate), d=1 / sampling_rate)

# Discretize the frequency axis into 1000 Hz intervals
freq_bins = np.arange(800, np.max(freq_axis), 1000)
fft_over_time = np.zeros((n_intervals, len(freq_bins) - 1))

# Calculate FFT over time
for i in range(n_intervals):
    start_idx = int(i * interval * sampling_rate)
    end_idx = int((i + 1) * interval * sampling_rate)
    if end_idx > len(sensor_values_1):
        end_idx = len(sensor_values_1)
    segment = sensor_values_1[start_idx:end_idx]
    fft_values = np.fft.fft(segment)
    segment = sensor_values_1[start_idx:end_idx]
    fft_values = np.fft.fft(segment)
    segment_freq = np.fft.fftfreq(len(segment), d=1 / sampling_rate)
    positive_freq_mask = segment_freq >= 800
    fft_values = np.abs(fft_values[positive_freq_mask])
    freq_axis = segment_freq[positive_freq_mask]
    for j in range(len(freq_bins) - 1):
        bin_mask = (freq_axis >= freq_bins[j]) & (freq_axis < freq_bins[j + 1])
        fft_over_time[i, j] = np.mean(fft_values[bin_mask])

print("FFT over time calculated")

# Plot the FFT over time
plt.pcolormesh(
    time_axis,
    freq_bins[:-1] / 1000,
    fft_over_time.T,
    shading="auto",
    edgecolors="grey",
    linewidth=0.075,
)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (kHz)")
plt.title("Short-Time Fourier Transform of Sensor 02")
plt.ylim(0.8, 65)
plt.xlim(0, max_time)
plt.colorbar(label="Amplitude")
plt.savefig(os.path.join(output_dir, "stft_02.svg"))
# plt.show()


# # Perform Fourier transform
# fft_values_1 = np.fft.fft(sensor_values_1)
# freq_1 = np.fft.fftfreq(len(sensor_values_1), time[1] - time[0])

# fft_values_2 = np.fft.fft(sensor_values_2)
# freq_2 = np.fft.fftfreq(len(sensor_values_2), time[1] - time[0])

# # Plot frequency spectrum
# positive_freq_mask_1 = freq_1 >= 1000
# positive_freq_mask_2 = freq_2 >= 1000
# plt.plot(freq_1[positive_freq_mask_1] / 1000, np.abs(fft_values_1)[positive_freq_mask_1])
# plt.plot(freq_2[positive_freq_mask_2] / 1000, np.abs(fft_values_2)[positive_freq_mask_2], alpha=0.5)
# plt.xlabel('Frequency (kHz)')
# plt.ylabel('Amplitude')
# plt.title('Frequency Spectrum Second Firing - Deflagration Setpoint')
# plt.xlim(0, 100)
# plt.ylim(0, 100000)
# plt.grid(True)
# plt.savefig('deflagration_setpoint_frequency_spectrum_02.png', dpi=600)
# #plt.show()
