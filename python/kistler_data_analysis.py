import pandas as pd
import matplotlib.pyplot as plt

# Load the data
raw_data_path = 'data/raw_data_txt/Medusa_02/deflagration/firing_02/Medusa_02_deflagration_02.txt'
output_csv_path = 'data/raw_data_csv/Medusa_02/deflagration/firing_02/Medusa_02_deflagration_02.csv'

# Read the data with whitespace separator
data = pd.read_csv(raw_data_path, sep=r'\s+', header=0)

# Save it as a CSV file
data.to_csv(output_csv_path, index=False)
print("File converted to CSV successfully.")

# # # Use if csv already exsists
# # data = pd.read_csv("data/raw_data_csv/Medusa_02/detonation/firing_03/Medusa_02_detonation_03.csv")

# # Re-zero time column s
# processed_data_sens = data.copy()
# min_value = processed_data_sens["s"].min()
# processed_data_sens["s"] = processed_data_sens["s"] - min_value

# # Time window of interest
# min_t = 3.6
# max_t = 4.7

# # Keep only important interval
# processed_data_sens = processed_data_sens[
#     (processed_data_sens["s"] >= min_t) & (processed_data_sens["s"] <= max_t)
# ]

# print("Starting to Plot")
# # Plot pC vs s
# plt.plot(processed_data_sens["s"], processed_data_sens["pC"])
# plt.xlabel("s")
# plt.ylabel("pC")
# plt.grid(True)
# plt.show()

# # # Save processed CSV
# # processed_output_path = "data/processed_data/Medusa_02/detonation/firing_03/Medusa_02_detonation_03_complete.csv"
# # processed_data_sens.to_csv(processed_output_path, index=False)
# # print("Processed file saved successfully.")