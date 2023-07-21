import matplotlib.pyplot as plt
import numpy as np
import argparse
from sorting_algorithms import *


def visualize_sorting(sort_algorithm):

    np.random.seed(0)
    data = np.random.randint(1, 100, 50)  # change 50 to desired amount of plots to sort

    plt.ion()  # interactive mode for live plotting
    plt.figure()
    bars = plt.bar(range(len(data)), data, align="center", alpha=0.5, color="Black")
    plt.title(f"{sort_algorithm.__name__}")  # Hacky way to inser name, idk I'm tired.
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

    for sorted_data in sort_algorithm(data):
        # Update the heights of the bars to reflect the current state of the array
        for bar, height in zip(bars, sorted_data):
            bar.set_height(height)
            bar.set_color( 
                c=np.random.rand(
                    3, 
                )
            ) # fun random colors, very important 

        plt.pause(0.1)  # Pause to show the updated plot

    # plt.ioff() # keep plot window open
    plt.pause(2)  # keep plot open for 1 sec
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize Sorting Algorithms.")
    parser.add_argument(
        "algorithm",
        type=str,
        choices=["bubble_sort", "insertion_sort", "chris_sort"],  # Add algorithms here
        help="The sorting algorithm to visualize.",
    )

    args = parser.parse_args()

    if args.algorithm == "bubble_sort":
        visualize_sorting(bubble_sort)
    elif args.algorithm == "insertion_sort":
        visualize_sorting(insertion_sort)
    elif args.algorithm == "chris_sort":
        visualize_sorting(chris_sort)

        # Update as needed
