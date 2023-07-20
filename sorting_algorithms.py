"""
Update with sorting algorithms for use with plot_sort.py

Much Fun! 
"""

# bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr  # yield returns the updated array at each step

# insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
        yield arr


# TODO: add more algorithms        