"""
Update with sorting algorithms for use with plot_sort.py

Much Fun! 

Resources:
- https://towardsdatascience.com/sorting-algorithms-with-python-4ec7081d78a1

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


# selection sort
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for index in range(i + 1, len(arr) - 1):
            if arr[index] < arr[min_index]:
                min_index = index
        arr[i], arr[min_index] = arr[min_index], arr[i]

        yield arr


# heap sort
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
        yield array


# TODO: add more algorithms
