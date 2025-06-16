import pytest

from src.leet_code.two_sum import Solution


class TestTwoSum:
    @pytest.mark.parametrize(
        "nums, target, output",
        [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ],
    )
    def test_maximum_difference(self, nums, target, output):
        solution = Solution()
        assert solution.two_sum(nums=nums, target=target) == output
