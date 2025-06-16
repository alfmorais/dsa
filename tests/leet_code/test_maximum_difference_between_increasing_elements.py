import pytest

from src.leet_code.maximum_difference_between_increasing_elements import Solution


class TestMaximumDifferenceBetweenIncreasingElements:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([7, 1, 5, 4], 4),
            ([9, 4, 3, 2], -1),
            ([1, 5, 2, 10], 9),
        ],
    )
    def test_maximum_difference(self, nums, expected):
        solution = Solution()
        assert solution.maximum_difference(nums=nums) == expected
