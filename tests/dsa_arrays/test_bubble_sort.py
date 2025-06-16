import pytest
from src.dsa_arrays.bubble_sort import bubble_sort


class TestBubbleSort:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([1], [1]),
            ([], []),
        ],
    )
    def test_bubble_sort(self, array, expected):
        bubble_sort(array)
        assert array == expected
