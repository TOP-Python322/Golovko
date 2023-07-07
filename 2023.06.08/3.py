def numbers_strip(
        numbers: list[float],
        n: int = 1,
        *,
        return_copy: bool = False
) -> list[float]:
    """Delete from list of numbers n minimal and n maximal
      numbers and return source list or its copy.

    """
    out_list = [x for x in numbers if x in sorted(numbers)[n:-n]]
    if return_copy:
        return out_list.copy()
    else:
        return out_list


'''
  9:41:47 > python -i 3.py
>>> sample = [17, 78, 67, 56, 1, 8, 100, 92, 40, 3]
>>> sample_stripped = numbers_strip(sample, 2, return_copy = True)
>>> sample_stripped
[17, 78, 67, 56, 8, 40]
>>> sample = [3, 4, 5, 6]
>>> sample_stripped = numbers_strip(sample)
>>> sample_stripped
[4, 5]
'''
