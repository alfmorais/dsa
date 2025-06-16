"""
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
"""

from typing import List


def bubble_sort(array: List[int]) -> None:
    array_size = len(array)

    for index in range(array_size - 1):
        swapped = False

        for second_index in range(array_size - index - 1):
            if array[second_index] > array[second_index + 1]:
                array[second_index], array[second_index + 1] = (
                    array[second_index + 1],
                    array[second_index],
                )
                swapped = True

        if not swapped:
            break


array = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"Unsorted array: {array}")

bubble_sort(array=array)
print(f"Sorted array: {array}")
