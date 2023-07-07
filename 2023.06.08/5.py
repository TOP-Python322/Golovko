def central_tendency(
        num1: float,
        num2: float,
        *numbers: float
) -> dict[str, float]:
    """Evaluate different statistic indicators for array of float numbers."""
    numbers = [num1, num2, *numbers]
    length = len(numbers)
    product = 1.0
    for i in numbers:
        product *= i
    arithmetic = sum(numbers) / length
    geometric = product ** (1 / length)
    harmonic = length / sum(1/x for x in numbers)
    numbers = sorted(numbers)
    if length % 2 == 1:
        median = float(numbers[length // 2])
    else:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    return {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }


'''
 10:15:15 > python -i 5.py
>>> central_tendency(1, 2, 3, 4)
{'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}
>>> sample = [1, 2, 3, 4, 5]
>>> central_tendency(*sample)
{'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
>>>
'''
