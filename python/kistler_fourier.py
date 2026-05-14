import os

import matplotlib.pyplot as plt
import numpy as np

### Need to adjust file path get infos from kistler_filtering.py

# Perform Fourier transform
fft_values_1 = np.fft.fft(sensor_values_1)
freq_1 = np.fft.fftfreq(len(sensor_values_1), time[1] - time[0])

fft_values_2 = np.fft.fft(sensor_values_2)
freq_2 = np.fft.fftfreq(len(sensor_values_2), time[1] - time[0])


# Filter out high frequency noise
fft_values_1[freq_1 < 1000] = 0
fft_values_2[freq_2 < 1000] = 0

for i in range(len(fft_values_2)):
    if 65000 < freq_2[i]:
        fft_values_2[i] = 0

# Perform inverse Fourier transform
reconstructed_signal = np.fft.ifft(fft_values_2)

# Extract the portion of the reconstructed signal for 4 < t < 4.4
mask = (time > 4) & (time < 4.4)
reconstructed_signal_segment = reconstructed_signal[mask]
reconstructed_signal_segment = np.real(reconstructed_signal_segment)

print(reconstructed_signal_segment)

# Save the reconstructed signal segment as a CSV file together with the time column
output_file_path = os.path.join(current_directory, "reconstructed_signal_segment.csv")
reconstructed_data = np.column_stack((time[mask], reconstructed_signal_segment))
np.savetxt(
    output_file_path,
    reconstructed_data,
    delimiter=",",
    header="Time,Reconstructed Signal",
    comments="",
)


# Plot frequency spectrum
print("Plotting frequency spectrum...")
positive_freq_mask_1 = freq_1 >= 0
positive_freq_mask_2 = freq_2 >= 0
plt.plot(
    freq_1[positive_freq_mask_1] / 1000, np.abs(fft_values_1)[positive_freq_mask_1]
)
plt.plot(
    freq_2[positive_freq_mask_2] / 1000,
    np.abs(fft_values_2)[positive_freq_mask_2],
    alpha=0.5,
)
plt.xlabel("Frequency (kHz)")
plt.ylabel("Amplitude")
plt.title("Frequency Spectrum Second Firing")
plt.xlim(0, 250)
plt.ylim(0, 100000)
plt.grid(True)
plt.show()

# Save the plot as a PNG file with 600 dpi
# output_file_path = os.path.join(current_directory, 'frequency_spectrum_02.png')
# plt.savefig(output_file_path, dpi=600)

# Plot both original and reconstructed signals
plt.plot(time, sensor_values_2, label="Original Signal")
# plt.plot(time, reconstructed_signal, label='Fourier Coefficients cancelled at 80 kHz and 200 kHz')
# plt.plot(time, filtered_signal_2, label='2nd Order Butterworth HP at 80 kHz and LP at 1 kHz')
# plt.plot(time, filtered_signal_1, label='4th Order Butterworth HP at 80 kHz and LP at 1 kHz')
# plt.plot(time[mask], reconstructed_signal_segment, label='Reconstructed Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
