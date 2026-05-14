import matplotlib.pyplot as plt
import pandas as pd

# data_1 = pd.read_csv(
#     "data/processed_data/Medusa_02/detonation/firing_04/filtered_signal_1.csv"
# )

data_2 = pd.read_csv(
    "data/processed_data/Medusa_02/detonation/firing_04/filtered_signal_2.csv"
)

# Define the time interval
# Aerospike: 3.93525
# Firing 04 (one wave): 0.4787299
# Firing 04 (counterrotating wave): 0.824685
# Firing 02 deflagration: 0.485

# start_time = 0
# end_time = start_time + 8

# # Filter the data
# mask = (data["time"] >= start_time) & (data["time"] <= end_time)
# filtered_data = data[mask]

# Plot both signals on the same axes
plt.plot(data_2["time"], data_2["value"], label="Signal 2")
# plt.plot(data_1["time"], data_1["value"], label="Signal 1")
plt.xlabel("Time [s]")
plt.ylabel("Dynamic Pressure [bar]")
plt.title("Detonation")
plt.grid(True)
# plt.legend()

# Save the plot as PNG
plt.savefig(
    "data/processed_data/Medusa_02/detonation/firing_04/detonation_complete.png",
    dpi=300,
    bbox_inches="tight",
)

# Save the filtered data as CSV
data_2.to_csv(
    "data/processed_data/Medusa_02/detonation/firing_04/detonation_complete.csv",
    index=False,
)

plt.show()
