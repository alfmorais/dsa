"""
Algorithm: Find The Lowest Value in an Array.
"""

from typing import List


def find_lowest_value(array: List[int]) -> int:
    lowest_value = array[0]

    for value in array:
        if value < lowest_value:
            lowest_value = value

    return lowest_value


array = [7, 12, 9, 11, 3]
print(find_lowest_value(array=array))
