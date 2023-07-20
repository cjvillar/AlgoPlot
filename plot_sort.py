import matplotlib.pyplot as plt
import numpy as np
import argparse
from sorting_algorithms import *
# # bubble sort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 yield arr  # yield returns the updated array at each step


# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         key_item = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key_item:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key_item
#         yield arr





def visualize_sorting(sort_algorithm):

    np.random.seed(0)
    data = np.random.randint(1, 100, 50)

    plt.ion()  # interactive mode for live plotting
    plt.figure()
    bars = plt.bar(range(len(data)), data, align="center", alpha=0.7, color="Black")
    plt.title(f"{sort_algorithm.__name__}")  # Hacky way to inser name, idk I'm tired.
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

    for sorted_data in sort_algorithm(data):
        # Update the heights of the bars to reflect the current state of the array
        for bar, height in zip(bars, sorted_data):
            bar.set_height(height)
        plt.pause(0.1)  # Pause to show the updated plot

    # keep plot window open
    plt.ioff()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize sorting algorithms.")
    parser.add_argument(
        "algorithm",
        type=str,
        choices=["bubble_sort", "insertion_sort"],  # Add algorithms here
        help="The sorting algorithm to visualize.",
    )

    args = parser.parse_args()

    if args.algorithm == "bubble_sort":
        visualize_sorting(bubble_sort)
    elif args.algorithm == "insertion_sort":
        visualize_sorting(insertion_sort)
        # Update as needed
