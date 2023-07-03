def math_function_resolver(
        # ИСПОЛЬЗОВАТЬ: многострочную запись при большом количестве аннотированных параметров
        func: 'function',
        # ИСПРАВИТЬ: для произвольных кортежа и словаря аннотируются только типы значений
        *x: tuple[int | float],
        strings: bool = False
) -> list[float | str]:
    # ИСПОЛЬЗОВАТЬ: специальный язык разметки reStructuredText для подробной документации
    """Calculate rounded results for different mathematical functions.

    :param func: the mathematical function as formula
    :param x: numbers, arguments of the function
    :param strings: specify the type of output as list of float numbers or strings
    """
    result = list(map(func, x))
    if strings:
        # ИСПОЛЬЗОВАТЬ: f-строки
        # result = [f'{x:.2f}' for x in result]
        # ИСПРАВИТЬ: в условии ничего не говорилось об округлении, следовательно его не должно быть
        result = ['{l:.2f}'.format(l=x) for x in result]
    return result


# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]

# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [1.5, 1.0, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5]

# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), strings=True)
# ['2.72', '7.40', '20.12', '54.74', '148.88', '404.96', '1101.49', '2996.07', '8149.30']


# ИТОГ: хорошо, доработать — 2/3
