import numpy as np

arr = np.array([8, 5, 6, 10])

# argsort gives the indices that would sort the array
order = np.argsort(arr)

sorted_arr = arr[order]


print("Original:", arr)
print("Sorted:", sorted_arr)
print("Track (positions):", order + 1)  # +1 if you want 1-based indexing
