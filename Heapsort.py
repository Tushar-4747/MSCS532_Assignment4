def heapify(arr, n, i):
    largest_value = i
    left_element = 2 * i + 1
    right_element = 2 * i + 2


    if left_element < n and arr[left_element] > arr[largest_value]:
        largest_value = left_element
    if right_element < n and arr[right_element] > arr[largest_value]:
        largest_value = right_element
    if largest_value != i:
        arr[i], arr[largest_value] = arr[largest_value], arr[i]
        heapify(arr, n, largest_value)

def heapsort_array(arr):
    n = len(arr)

    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# added random values
arr = [56, 10, 40, 80, 5, 58, 25, 89]

print("Befor Sorting", arr)
heapsort_array(arr)

# Display Sorted Value
print("After Sorting array is", arr)
