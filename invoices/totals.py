def gst_total(amount: float, rate: float = 0.18) -> float:
    return round(amount * (1 + rate), 2)
