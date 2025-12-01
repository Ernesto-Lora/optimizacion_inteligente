import numpy as np
import matplotlib.pyplot as plt

# Approximate coordinates extracted from the image
# Format: (x, y)
coordinates = [
    (2, 60),    # Far left point
    (14, 32),   # Bottom left-ish point
    (16, 66),   # Top left point
    (35, 26),   # Lower middle point
    (47, 16),   # Lowest point (bottom center)
    (57, 53),   # Middle right point
    (94, 80)    # Top right point
]

# Separating into X and Y lists for easy plotting/calculation
x_vals = [pt[0] for pt in coordinates]
y_vals = [pt[1] for pt in coordinates]

# --- Verification Code (Optional) ---
# This plots the points so you can compare with your original image
plt.figure(figsize=(5, 5))
plt.plot(x_vals, y_vals, 'bs', markersize=8, label='Points') # Blue squares
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.grid(True)
plt.title("Reconstructed Points")
plt.show()

print("Coordinates List:", coordinates)