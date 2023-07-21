"""
Update with sorting algorithms for use with plot_sort.py

Much Fun! 
"""
from random import randint


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

 # a nonsensical sorting algorithm
def chris_sort(arr):
   
    for i in range(len(arr)):
        sort = sorted(arr)
        yield sort[i::-1] 
    yield sort[:]


# selection sort WORK IN PROGRESS
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for index in range(i + 1, len(arr)-1):
            if arr[index] < arr[min_index]:
                min_index = index
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        yield arr
    
    
# TODO: add more algorithms
