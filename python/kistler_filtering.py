import numpy as np
import os
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# Load sensor data from CSV file
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'data/processed_data/Medusa_02/deflagration/firing_02/Medusa_02_deflagration_02_complete.csv')
output_directory = os.path.dirname(file_path)  # Get the directory of the input file

data = np.genfromtxt(file_path, delimiter=',')

# Extract time and sensor values
time = data[1:, 0]
sensor_values_1 = data[1:, 1]
sensor_values_2 = data[1:, 2]

# Define the filter parameters
order_1 = 4  # Filter order
cutoff_freq_low = 65000  # Low-pass cutoff frequency in Hz
cutoff_freq_high = 1000  # High-pass cutoff frequency in Hz

# Normalize the cutoff frequencies
nyquist_freq = 0.5 * (1 / (time[1] - time[0]))
normalized_cutoff_freq_low = cutoff_freq_low / nyquist_freq
normalized_cutoff_freq_high = cutoff_freq_high / nyquist_freq

# Design the Butterworth low-pass filter
b_1_low, a_1_low = butter(order_1, normalized_cutoff_freq_low, btype='low', analog=False, output='ba')

# Design the Butterworth high-pass filter
b_1_high, a_1_high = butter(order_1, normalized_cutoff_freq_high, btype='high', analog=False, output='ba')

# Apply the zero-phase Butterworth filters to sensor_values_2
filtered_signal_1_low = filtfilt(b_1_low, a_1_low, sensor_values_2)
filtered_signal_1 = filtfilt(b_1_high, a_1_high, filtered_signal_1_low)

# Save the filtered signal values of sensor_values_2
output_file_path_filtered_2 = os.path.join(output_directory, 'filtered_signal_2.csv')
filtered_data_2 = np.column_stack((time, filtered_signal_1))
np.savetxt(output_file_path_filtered_2, filtered_data_2, delimiter=',', header='time,value', comments='')

# Apply the zero-phase Butterworth filters to sensor_values_1
filtered_signal_1_low_1 = filtfilt(b_1_low, a_1_low, sensor_values_1)
filtered_signal_1_1 = filtfilt(b_1_high, a_1_high, filtered_signal_1_low_1)

# Save the filtered signal values of sensor_values_1
output_file_path_filtered_1 = os.path.join(output_directory, 'filtered_signal_1.csv')
filtered_data_1 = np.column_stack((time, filtered_signal_1_1))
np.savetxt(output_file_path_filtered_1, filtered_data_1, delimiter=',', header='time,value', comments='')

# Plot both original and reconstructed signals
plt.plot(time, sensor_values_2, label='Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()