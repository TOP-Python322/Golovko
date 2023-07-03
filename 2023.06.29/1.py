# ===== 1 =====


from collections.abc import Iterable


def product(numbers: Iterable[float]) -> float:
    """Recursive multiplication of numbers range"""
    if len(numbers) == 1:
        comp = numbers[0]
    else:
        comp = numbers[0] * product(numbers[1:])
    return float(comp)


'''
>>> product(range(10, 60, 10))
12000000.0
>>> product((0.12, 0.05, -0.09, 0.0, 0.21))
-0.0
'''
