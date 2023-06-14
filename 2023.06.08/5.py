# ===== 5 =====


from math import pow, floor


def central_tendency(num1 : float, num2 : float, *numbers : float) -> dict[str, float] | None:
    """Evaluate different statistic indicators for array of float numbers"""
    in_numbers = [num1, num2, *numbers]
    length = len(in_numbers)
    comp = 1.0
    for i in in_numbers:
        comp *= i
    arithmetic = sum(in_numbers) / length
    geometric = pow(comp, 1 / length)
    harmonic = length / sum([1 / x for x in in_numbers])

    sorted_numbers = sorted(in_numbers)
    if length % 2 == 1:
        median = float(sorted_numbers[floor(length / 2)])
    else:
        median = float((sorted_numbers[int(length / 2) - 1] + sorted_numbers[int(length / 2)]) / 2)
    out_dict = {'median': median, 'arithmetic': arithmetic, 'geometric': geometric, 'harmonic': harmonic}
    return out_dict


'''
>>> central_tendency(1, 2, 3, 4) 
{'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}

>>> sample = [1, 2, 3, 4, 5]
>>> central_tendency(*sample)
{'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
''' 
