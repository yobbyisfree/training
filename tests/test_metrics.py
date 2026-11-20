import pytest

from training.metrics import capacity_factor


def test_basic() -> None:
    # 100kW 설비가 24시간 동안 600kWh를 발전하면 이용률은 0.25
    assert capacity_factor(600, 100, 24) == 0.3


def test_zero_capacity_is_error() -> None:
    # 설비용량이 0이면 계산할 수 없으니 오류가 나야 한다
    with pytest.raises(ValueError):
        capacity_factor(600, 0, 24)
