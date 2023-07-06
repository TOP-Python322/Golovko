def math_function_resolver(
        func: 'function',
        *x: int | float,
        strings: bool = False
) -> list[float | str]:
    """Calculate rounded results for different mathematical
      functions.

    :param func: the mathematical function as formula
    :param x: numbers, arguments of the function
    :param strings: specify the type of output as list of float
      numbers or strings

    """
    result = list(map(func, x))
    if strings:
        result = [f'{x}' for x in result]
    return result


'''
 14:03:18 > python -i 3.py
>>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
[2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]
>>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
[1.5, 1.0, 0.5, 0.0, -0.5, -1.0, -1.5, -2.0, -2.5]
>>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), strings=True)
['2.72', '7.398400000000001', '20.123648000000003', '54.73632256000002',
'148.88279736320004', '404.96120882790416', '1101.4944880118994',
'2996.0650073923666', '8149.296820107238']
'''
