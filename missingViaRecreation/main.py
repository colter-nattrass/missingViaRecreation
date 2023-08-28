from classes.dataSimulator import Point, SimulatedThicknessValue
import pandas as pd
import matplotlib.pyplot as plt
import math


#Create random points with boundary of wafer edge

random_points = [Point.generate_random_point().rotate_by_radians(math.pi/2) for _ in range(100)]

data = {"x": [point.x for point in random_points],
        "y": [point.y for point in random_points]}

df_rda = pd.DataFrame(data)


#Store data in CSV in the project
data_rda_csv = "../data/data_rda.csv"
df_rda.to_csv(data_rda_csv, index=True)

box_length = 3
box_height = 3
box_corners = [point.draw_box_around_point(box_length, box_height) for point in random_points]

corner_names = ["top_left", "top_right", "bottom_left", "bottom_right"]
for i, corner_name in enumerate(corner_names):
    df_rda[corner_name + "_x"] = [corner[i].x for corner in box_corners]
    df_rda[corner_name + "_y"] = [corner[i].y for corner in box_corners]

# This is where I would input the LotID, WaferID and corresponding x, y for the box in the API to return the aggregate thickness within that box.
# For the purposes of the presentation I will also simulate the thicknesses

simulated_value = SimulatedThicknessValue()

simulated_values = [simulated_value.generate_value() for _ in range(100)]
print(simulated_value)
df_rda["simulated_value"] = simulated_values

# Calculate how many points were beyond the +/- 5 limit
beyond_limit_count = df_rda[df_rda["simulated_value"].abs() > 25].shape[0]

simulated_mean = df_rda["simulated_value"].mean()
simulated_median = df_rda["simulated_value"].median()

print("Simulated Mean:", simulated_mean)
print("Simulated Median:", simulated_median)

# Create a histogram plot from DataFrame
plt.hist(df_rda["simulated_value"], bins=20, edgecolor="k")
plt.axvline(x=15, color='r', linestyle='--', label='Limit = 15')
plt.axvline(x=25, color='g', linestyle='--', label='Limit = 25')
plt.xlabel("Simulated Values")
plt.ylabel("Frequency")
plt.title("Histogram of Simulated Values")

# Add statistics as text annotations
plt.text(10, 25, f"Mean: {simulated_mean:.2f}", fontsize=10)
plt.text(10, 20, f"Median: {simulated_median:.2f}", fontsize=10)

plt.show()