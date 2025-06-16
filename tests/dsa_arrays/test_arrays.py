import pytest
from src.dsa_arrays.arrays import find_lowest_value


class TestFindLowestValue:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([3, 2, 1], 1),
            ([10, -1, 5], -1),
            ([0, 0, 0], 0),
            ([7], 7),
            ([100, 20, 30, 5], 5),
        ],
    )
    def test_find_lowest_value(self, array, expected):
        result = find_lowest_value(array)
        assert result == expected
