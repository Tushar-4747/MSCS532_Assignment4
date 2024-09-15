import time
import random

def generate_arrays(size):
    arr_random = random.sample(range(size * 10), size)#Random 
    arr_sorted = sorted(arr_random)# Sorted 
    arr_reverse_sorted = sorted(arr_random, reverse=True)# Reverse sorted 
    return arr_random, arr_sorted, arr_reverse_sorted

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid_element = len(arr) // 2
        left_element = arr[:mid_element]
        right_element = arr[mid_element:]
        merge_sort(left_element)
        merge_sort(right_element)
        i = j = k = 0
        while i < len(left_element) and j < len(right_element):
            if left_element[i] < right_element[j]:
                arr[k] = left_element[i]
                i += 1
            else:
                arr[k] = right_element[j]
                j+=1
            k += 1
        while i < len(left_element):
            arr[k] = left_element[i]
            i += 1
            k += 1
        while j < len(right_element):
            arr[k] = right_element[j]
            j += 1
            k += 1

# Heapsort Function 
def heapify(arr, n, i):
    largest = i  
    left_element = 2 * i + 1  
    right_element = 2 * i + 2  

    if left_element < n and arr[left_element] > arr[largest]:
        largest = left_element
    if right_element < n and arr[right_element] > arr[largest]:
        largest = right_element
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

# Quicksort Function
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left_element = [x for x in arr if x < pivot]
    mid_elementdle = [x for x in arr if x == pivot]
    right_element = [x for x in arr if x > pivot]
    return quicksort(left_element) + mid_elementdle + quicksort(right_element)


#comparing all sorting
def compare_sorts():
    sizes = [500, 3000, 75000, 13000, 16500]
    for size in sizes:
        arr_random, arr_sorted, arr_reverse_sorted = generate_arrays(size)

        for distribution, arr in zip(["Random", "Sorted", "Reverse-sorted"], [arr_random, arr_sorted, arr_reverse_sorted]):
            print(f"\nSize of Array: {size}, Distribution: {distribution}")

            # Merge Sort
            start_time = time.time()
            merge_sort(arr.copy())
            end_time = time.time()
            print(f"Time of Merge Sort: {end_time - start_time:.6f} seconds")

             # Quicksort
            start_time = time.time()
            quicksort(arr.copy())
            end_time = time.time()
            print(f"Time of Quicksort: {end_time - start_time:.6f} seconds")

            # Heapsort
            start_time = time.time()
            heapsort(arr.copy())
            end_time = time.time()
            print(f"Time of Heapsort: {end_time - start_time:.6f} seconds")

            # Timsort 
            start_time = time.time()
            sorted(arr.copy())  
            end_time = time.time()
            print(f"Time of Timsort: {end_time - start_time:.6f} seconds")

# compare sorting algorithm
compare_sorts()
