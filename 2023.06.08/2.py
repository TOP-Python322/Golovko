def taxi_cost(length: int, wait: int = 0) -> int | None:
    """Calculate cost of trip on two parameters,
    length of driveway and waiting time.

    """
    if length < 0 or wait < 0:
        return None
    if length == 0:
        cost = 80 + 80 + wait * 3
    else:
        cost = 80 + round(length / 150) * 6 + wait * 3
    return cost


'''
  9:01:31 > python -i 2.py
>>> taxi_cost(1500)
140
>>> taxi_cost(2560)
182
>>> taxi_cost(0, 5)
175
>>> taxi_cost(42130, 8)
1790
>>> taxi_cost(-300)
>>>
'''
