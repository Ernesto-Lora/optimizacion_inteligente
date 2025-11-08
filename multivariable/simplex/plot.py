import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# 1. Define the function (Himmelblau's function)
def f(x1, x2):
    """The function to be plotted."""
    term1 = (x1**2 + x2 - 11)**2
    term2 = (x1 + x2**2 - 7)**2
    return term1 + term2

# 2. Set up the grid
# Create 1D arrays for x1 and x2 from -5 to 5
x1_range = np.linspace(-5, 5, 400)
x2_range = np.linspace(-5, 5, 400)

# Create the 2D grid
X1, X2 = np.meshgrid(x1_range, x2_range)

# 3. Evaluate the function on the grid
Z = f(X1, X2)

# 4. Create the plot
print("Generating plot...")
fig, ax = plt.subplots(figsize=(8, 7))

# --- Create the Heatmap (Filled Contour) ---
# Use a logarithmic color scale for better visibility, as the
# function's values span several orders of magnitude.
# We add a small value (1e-1) to avoid log(0).
norm = colors.LogNorm(vmin=Z.min() + 0.1, vmax=Z.max())
levels = np.logspace(np.log10(Z.min() + 0.1), np.log10(Z.max()), 20)

# contourf creates the filled "heatmap"
cp = ax.contourf(X1, X2, Z, levels=levels, norm=norm, cmap='viridis')

# Add a color bar to show the values
cbar = fig.colorbar(cp, ax=ax, label='f(x1, x2) Value')

# --- Add Contour Lines (like the example image) ---
# We can use some of the same levels from your image for the lines
line_levels = [3, 10, 30, 60, 100, 150, 250, 450]

# contour draws the lines
contours = ax.contour(X1, X2, Z, levels=line_levels, colors='black', linewidths=0.7)

# Add labels directly onto the contour lines
ax.clabel(contours, inline=True, fontsize=8, fmt='%1.0f')

# 5. Style and Save the Plot
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title("Contour Plot of f(x1, x2) = (x₁²+x₂-11)² + (x₁+x₂²-7)²")

# Set the limits and aspect ratio
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal', 'box')

# Save the plot to a PDF file
try:
    plt.savefig('functionplot.pdf')
    print("Plot successfully saved as 'functionplot.pdf'")
except Exception as e:
    print(f"Error saving file: {e}")

# Optionally, display the plot
# plt.show()