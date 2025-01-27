import random
import time

# Randomized Quicksort Implementation
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Choose pivot randomly
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # Swap pivot with last element
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    while low < high:
        pi = randomized_partition(arr, low, high)
        # Recursively sort the smaller partition first
        if (pi - low) < (high - pi):
            randomized_quicksort(arr, low, pi - 1)
            low = pi + 1  # Iterate on the larger partition
        else:
            randomized_quicksort(arr, pi + 1, high)
            high = pi - 1  # Iterate on the larger partition

# Deterministic Quicksort Implementation
def deterministic_partition(arr, low, high):
    pivot = arr[high]  # Always choose the last element as the pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    while low < high:
        pi = deterministic_partition(arr, low, high)
        # Recursively sort the smaller partition first
        if (pi - low) < (high - pi):
            deterministic_quicksort(arr, low, pi - 1)
            low = pi + 1  # Iterate on the larger partition
        else:
            deterministic_quicksort(arr, pi + 1, high)
            high = pi - 1  # Iterate on the larger partition

# Empirical Comparison
def compare_quicksort():
    input_sizes = [100, 1000, 5000, 10000]
    for size in input_sizes:
        print(f"\nArray Size: {size}")
        
        # Generate input arrays
        random_array = [random.randint(1, 10000) for _ in range(size)]
        sorted_array = sorted(random_array)
        reverse_sorted_array = sorted_array[::-1]
        repeated_array = [5] * size

        # Test Randomized Quicksort
        for arr, desc in [(random_array[:], "Random"), (sorted_array[:], "Sorted"), 
                          (reverse_sorted_array[:], "Reverse Sorted"), (repeated_array[:], "Repeated")]:
            start_time = time.time()
            randomized_quicksort(arr, 0, len(arr) - 1)
            print(f"Randomized Quicksort ({desc}): {time.time() - start_time:.4f}s")

        # Test Deterministic Quicksort
        for arr, desc in [(random_array[:], "Random"), (sorted_array[:], "Sorted"), 
                          (reverse_sorted_array[:], "Reverse Sorted"), (repeated_array[:], "Repeated")]:
            start_time = time.time()
            deterministic_quicksort(arr, 0, len(arr) - 1)
            print(f"Deterministic Quicksort ({desc}): {time.time() - start_time:.4f}s")

if __name__ == "__main__":
    compare_quicksort()