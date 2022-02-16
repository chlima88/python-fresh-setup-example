from .contas import soma


def test_soma():
    """Testing soma"""

    result = soma(2, 3)

    assert result == 5
