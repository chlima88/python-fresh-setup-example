from .calc import sum_num


def test_sum_num():
    """Testing soma"""

    result = sum_num(2, 3)

    assert result == 5
