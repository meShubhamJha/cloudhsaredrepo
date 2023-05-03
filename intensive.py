import numpy as np
import time

# Generate a large array of random numbers
arr = np.random.rand(200, 200)

# Perform a matrix multiplication using NumPy
start_time = time.time()
result = np.dot(arr, arr)
end_time = time.time()

# Print the time taken to perform the operation
print("Time taken:", end_time - start_time, "seconds")
