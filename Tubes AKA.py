import time
import random
import matplotlib.pyplot as plt

# Fungsi untuk pencarian linear
def linear_search_iteratif(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Fungsi untuk pencarian biner
def binary_search_iteratif(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Fungsi untuk pencarian biner rekursif
def binary_search_rekursif(data, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search_rekursif(data, target, mid + 1, high)
    else:
        return binary_search_rekursif(data, target, low, mid - 1)

# Pencarian Linear (Rekursif)
def linear_search_rekursif(data, target, index=0):
    if index >= len(data):
        return -1
    if data[index] == target:
        return index
    return linear_search_rekursif(data, target, index + 1)

# Fungsi untuk mengukur waktu eksekusi
def measure_time(func, *args, iterations=10):
    start_time = time.perf_counter()
    for _ in range(iterations):
        func(*args)
    end_time = time.perf_counter()
    return (end_time - start_time) / iterations



# Main program
if __name__ == "__main__":
    # Ukuran data
    data_size = np.arange(0, 1001, 100)  # Data sizes from 0 to 1000 in steps of 100
    linear_iterative = []
    linear_recursive = []
    binary_iterative = []
    binary_recursive = []

    for size in data_sizes:
        print(f"\nData size: {size}")
        
    for n in data_size:
        arr = list(range(n))
        target = n - 1  # Target is the last element
    
        # Measure times
        linear_iterative.append(measure_time_search(linear_search_iterative, arr, target))
        linear_recursive.append(measure_time_search(linear_search_recursive, arr, target))
        binary_iterative.append(measure_time_search(binary_search_iterative, arr, target))
        binary_recursive.append(measure_time_search(binary_search_recursive, arr, target, 0, len(arr) - 1))
        
        # --- Linear Search ---
       def plot_search_comparison(data_range, title):
    plt.figure(figsize=(10, 6))
    mask = data_size <= data_range  # Filter data for the specified range
    plt.plot(data_size[mask], np.array(linear_iterative)[mask], label="Linear Search Iterative", marker='o', color='orange')
    plt.plot(data_size[mask], np.array(linear_recursive)[mask], label="Linear Search Recursive", marker='o', color='red')
    plt.plot(data_size[mask], np.array(binary_iterative)[mask], label="Binary Search Iterative", marker='o', color='blue')
    plt.plot(data_size[mask], np.array(binary_recursive)[mask], label="Binary Search Recursive", marker='o', color='magenta')

    # Add labels, title, and legend
    plt.title(title, fontsize=14)
    plt.xlabel("Data Size", fontsize=12)
    plt.ylabel("Time (seconds)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Plot for data range 0-1000
plot_search_comparison(1000, "Search Time Comparison: Linear vs Binary (0-1000)")

# Plot for data range 0-200
plot_search_comparison(200, "Search Time Comparison: Linear vs Binary (0-200)")

# Plot for data range 0-400
plot_search_comparison(400, "Search Time Comparison: Linear vs Binary (0-400)")
