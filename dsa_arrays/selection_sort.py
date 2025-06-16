"""
The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
"""

from typing import List


def selection_sort(array: List[int]) -> None:
    array_size = len(array)

    for index in range(array_size - 1):
        minimum_index = index

        for second_index in range(index + 1, array_size):
            if array[second_index] < array[minimum_index]:
                minimum_index = second_index

        array[index], array[minimum_index] = array[minimum_index], array[index]


array = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"Unsorted array: {array}")

selection_sort(array=array)
print(f"Sorted array: {array}")
