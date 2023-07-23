"""
Usage: python plot_sort.py <algorithm> <data size>
Example: python plot_sort.py heap_sort 20

"""


import matplotlib.pyplot as plt
import numpy as np
import argparse
from sorting_algorithms import *


def visualize_sorting(sort_algorithm, size):
    data = np.random.randint(
        1, 100, size
    )  # change 50 to desired amount of plots to sort
    bars = plt.bar(range(len(data)), data, align="center", alpha=0.5)
    plt.title(
        f"{sort_algorithm.__name__}"
    )  # Hacky way to insert sort algo name, idk I'm tired.
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.ion()

    for sorted_data in sort_algorithm(data):
        # Update the heights of the bars to reflect the current state of the array
        for bar, height in zip(bars, sorted_data):
            bar.set_height(height)
            # bar.set_color(
            #     c=np.random.rand(
            #         4,
            #     )
            # ) # fun random colors, very important

        plt.pause(0.1)  # Pause to show the updated plot

    # plt.ioff() # keep plot window open
    plt.pause(2)  # keep plot open for 1 sec
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize Sorting Algorithms.")
    parser.add_argument(
        "algorithm",
        type=str,
        default=50,
        help="The sorting algorithm to visualize.",
    )
    parser.add_argument(
        "size",
        type=int,
        help="The size of data to sort. default 50",
    )

    args = parser.parse_args()

    size = args.size
    algorithms = {
        "bubble_sort": bubble_sort,
        "insertion_sort": insertion_sort,
        "chris_sort": chris_sort,
        "selection_sort": selection_sort,
        "heap_sort": heap_sort,
        # Add more algorithms here
    }

    if args.algorithm in algorithms:
        visualize_sorting(algorithms[args.algorithm], args.size)
    else:
        print("Invalid algorithm name. Please choose from available algorithms.")
