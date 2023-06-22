# ИСПОЛЬЗОВАТЬ: длинные списки параметров (обычно больше двух, особенно с аннотациями) записывают вертикально
def numbers_strip(
        # ИСПРАВИТЬ: вы ожидаете не просто произвольный список, а список именно чисел — следует указать это в аннотации
        numbers: list,
        n: int = 1,
        # ПЕРЕИМЕНОВАТЬ: переменным требуется давать имена по смыслу, так чтобы читать код было удобнее и быстрее — имя toggle ничего не говорит о том, какое значение ассоциировано с данной переменной, вместо него стоило назвать переменную copy или даже return_copy
        toggle: bool = False
# ИСПРАВИТЬ: аннотируйте вовзрат списка именно чисел (в т.ч. вещественных)
) -> list:
    """Delete from list of numbers n minimal and n maximal numbers and return source list or its copy."""
    if toggle:
        # sort_list = sorted(numbers)
        # sort_list = sort_list[n:-n]
        # ИСПОЛЬЗОВАТЬ: можно записать короче
        sort_list = sorted(numbers)[n:-n]
        out_list = [x for x in numbers if x in sort_list]
        return out_list
    else:
        # ИСПРАВИТЬ: внимательнее читайте условие: к копии списка применяются все те же изменения
        return numbers.copy()


# >>> sample = [17, 78, 67, 56, 1, 8, 100, 92, 40, 3]
# >>> sample_stripped = numbers_strip(sample, 2, toggle = True)
# >>> sample_stripped
# [17, 78, 67, 56, 8, 40]

# >>> sample = [3, 4, 5, 6]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# КОММЕНТАРИЙ: а должно быть [4, 5]
# [3, 4, 5, 6]


# ИТОГ: задача понята неверно, переработать — 2/6
