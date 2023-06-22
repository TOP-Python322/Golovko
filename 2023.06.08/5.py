from math import pow, floor


def central_tendency(
        num1: float,
        num2: float,
        *numbers: float
# ИСПРАВИТЬ: данная функция не возвращает None
) -> dict[str, float] | None:
    """Evaluate different statistic indicators for array of float numbers."""
    # ПЕРЕИМЕНОВАТЬ: исходный кортеж numbers более не используется, а значит может быть перезаписан — создание ещё одной переменной in_numbers избыточно
    in_numbers = [num1, num2, *numbers]
    length = len(in_numbers)
    # ПЕРЕИМЕНОВАТЬ: произведение чисел — product
    comp = 1.0
    for i in in_numbers:
        comp *= i
    arithmetic = sum(in_numbers) / length
    # КОММЕНТАРИЙ: существует оператор возведения в степень **
    geometric = pow(comp, 1 / length)
    # ИСПРАВИТЬ: функция sum() прекрасно работает и с чистыми генераторными выражениями, в создании списка нет необходимости
    harmonic = length / sum([1/x for x in in_numbers])

    # ПЕРЕИМЕНОВАТЬ: ещё одна лишняя переменная sorted_numbers
    sorted_numbers = sorted(in_numbers)
    if length % 2 == 1:
        # ИСПРАВИТЬ: точно такого же эффекта, как и с функцией floor(), можно добиться используя оператор целочисленного деления // — убедитесь самостоятельно
        median = float(sorted_numbers[floor(length / 2)])
    else:
        # ИСПРАВИТЬ: используйте оператор // вместо int()
        # ИСПРАВИТЬ: использование функции float() избыточно — оператор вещественного деления / всегда возвращает объект float
        median = float((sorted_numbers[int(length/2)-1] + sorted_numbers[int(length/2)]) / 2)
    # out_dict = {'median': median, 'arithmetic': arithmetic, 'geometric': geometric, 'harmonic': harmonic}
    # return out_dict
    # ИСПОЛЬЗОВАТЬ: создание переменной out_dict избыточно, а большинство словарных литералов удобнее читать, если они записаны вертикально
    return {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }


# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.9200000000000004}

# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}


# ИТОГ: в целом довольно хорошо, но базовые инструменты стоит изучить подробнее — 3/4
