import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/processed_data/Medusa_02/detonation/firing_04/filtered_signal_1.csv")

# Define the time interval
# Aerospike: 3.93525
# Firing 04 (one wave): 0.4787299
# Firing 04 (counterrotating wave): 0.824685
# Firing 02 deflagration: 0.485

start_time = 0.824685
end_time = start_time + 0.001

# Filter the data
mask = (data["time"] >= start_time) & (data["time"] <= end_time)
filtered_data = data[mask]

# Plot the filtered data
plt.plot(filtered_data["time"], filtered_data["value"])
plt.xlabel("Time [s]")
plt.ylabel("Dynamic Pressure [bar]")
plt.title("Detonation with Counterrotating Waves")
plt.grid(True)

# Save the plot as PNG
plt.savefig("data/processed_data/Medusa_02/detonation/firing_04/counterrotating_waves.png", dpi=300, bbox_inches='tight')

# Save the filtered data as CSV
filtered_data.to_csv("data/processed_data/Medusa_02/detonation/firing_04/counterrotating_waves.csv", index=False)

plt.show()