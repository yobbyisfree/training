"""발전 설비 지표 계산."""


def capacity_factor(generation_kwh: float, capacity_kw: float, hours: float) -> float:
    """이용률 = 실제 발전량 / (설비용량 x 시간).

    예: 100kW 설비가 24시간 동안 600kWh를 발전하면 0.25.
    """
    if capacity_kw <= 0:
        raise ValueError("설비용량은 0보다 커야 합니다")
    if hours <= 0:
        raise ValueError("시간은 0보다 커야 합니다")
    return generation_kwh / (capacity_kw * hours)
