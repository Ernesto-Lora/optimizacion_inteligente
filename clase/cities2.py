import numpy as np
import matplotlib.pyplot as plt

# 1. Define coordinates (from previous step)
coordinates = [
    (2, 60),    # City 0
    (14, 32),   # City 1
    (16, 66),   # City 2
    (35, 26),   # City 3
    (47, 16),   # City 4
    (57, 53),   # City 5
    (94, 80)    # City 6
]

# Convert to numpy array for easier mathematical operations
coords_np = np.array(coordinates)
num_cities = len(coords_np)

# --- Setup Plot ---
plt.figure(figsize=(10, 6)) # Large figure size so labels don't overlap too much
plt.xlim(0, 100)
plt.ylim(10, 81)
plt.grid(True, linestyle='--', color='gray', alpha=0.5)
plt.xticks(range(0, 101, 10))
plt.yticks(range(10, 81, 10))

# --- Calculate and Plot Edges (Distances) ---
# We iterate through every unique pair of cities
print("Calculating distances between all pairs:")

for i in range(num_cities):
    # Start j from i + 1 so we don't double count pairs (e.g., 0-1 vs 1-0)
    # and don't connect a city to itself (0-0)
    for j in range(i + 1, num_cities):
        p1 = coords_np[i]
        p2 = coords_np[j]

        # Calculate Euclidean distance: sqrt((x2-x1)^2 + (y2-y1)^2)
        # np.linalg.norm does this automatically for vectors
        distance = np.linalg.norm(p1 - p2)

        # Print calculation to console (optional)
        # print(f"Distance City {i} to City {j}: {distance:.2f}")

        # 1. Plot the straight line edge
        # Using alpha=0.3 makes the lines semi-transparent so it's less messy
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', linewidth=1, alpha=0.3)

        # 2. Add distance label at the midpoint of the line
        midpoint_x = (p1[0] + p2[0]) / 2
        midpoint_y = (p1[1] + p2[1]) / 2

        # We use a small white box around the text so it's readable over the lines
        bbox_props = dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8)
        plt.text(midpoint_x, midpoint_y, f"{distance:.1f}",
                 fontsize=14, ha='center', va='center', bbox=bbox_props, color='darkred')

# --- Plot City Points on top ---
# zorder ensures points are drawn on top of lines
plt.plot(coords_np[:, 0], coords_np[:, 1], 'bs', markersize=10, zorder=5)

# Add labels to the cities (0, 1, 2...) for easier reference
for i, (x, y) in enumerate(coordinates):
    plt.text(x + 1.5, y + 1.5, str(i), fontsize=14, fontweight='bold', color='blue', zorder=6)


plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.tight_layout()
plt.savefig("cities.pdf")
plt.show()