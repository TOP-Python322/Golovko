# ИСПОЛЬЗОВАТЬ: длинные списки параметров (обычно больше двух, особенно с аннотациями) записывают вертикально
def numbers_strip(
        numbers: list,
        n: int = 1,
        toggle: bool = False
) -> list:
    """Delete from list of numbers n minimal and n maximal numbers and return source list or its copy."""
    if toggle:
        sort_list = sorted(numbers)
        sort_list = sort_list[n:-n]
        out_list = [x for x in numbers if x in sort_list]
        return out_list
    else:
        return numbers.copy()


# >>> sample = [17, 78, 67, 56, 1, 8, 100, 92, 40, 3]
# >>> sample_stripped = numbers_strip(sample, 2, toggle = True)
# >>> sample_stripped
# [17, 78, 67, 56, 8, 40]


