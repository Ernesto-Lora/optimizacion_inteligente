import math
import json
import os

# 1. Your specific coordinates (City 0 to 6)
cities = {
    0: (2, 60),
    1: (14, 32),
    2: (16, 66),
    3: (35, 26),
    4: (47, 16),
    5: (57, 53),
    6: (94, 80)
}

# 2. Function to calculate Euclidean distance
def get_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 3. Generate the data structure
# We use a dictionary of dictionaries to preserve the order and mapping
distance_matrix = {}

for i in sorted(cities.keys()):
    distance_matrix[i] = {}
    for j in sorted(cities.keys()):
        if i == j:
            distance_matrix[i][j] = 0.0
        else:
            # Calculate and round to 4 decimal places
            d = get_dist(cities[i], cities[j])
            distance_matrix[i][j] = round(d, 4)

# 4. Save to a local file (JSON format)
file_name = "city_distances.json"

try:
    with open(file_name, "w") as f:
        # indent=4 makes the file human-readable
        json.dump(distance_matrix, f, indent=4)
    
    print(f"✅ Success! Data saved to: {os.path.abspath(file_name)}")
    print("You can now load this file in your heuristic algorithm script.")

except IOError as e:
    print(f"❌ Error saving file: {e}")

# --- PREVIEW OF DATA ---
# This just shows you what was saved
print("\nPreview of City 0 distances:")
print(distance_matrix[0])