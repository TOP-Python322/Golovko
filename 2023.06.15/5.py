def logger(func):
    """Return the actual function-logger to stdout of called function

    :param func: a called function

    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            size = func.__code__.co_argcount
            if size:
                args_list = [None] * size
                if func.__defaults__:
                    args_list = [f'{x}' for x in func.__defaults__]
                    for i in range(size - len(func.__defaults__)):
                        args_list.insert(0, ' ')
                for i in range(len(args)):
                    args_list[i] = f'{args[i]}'
                args = ', '.join(args_list)
            else:
                args = ''

            if func.__kwdefaults__:
                if kwargs:
                    for key, _ in kwargs.items():
                        func.__kwdefaults__[key] = kwargs[key]
                kwargs = []
                for key, value in func.__kwdefaults__.items():
                    kwargs.append(f'{key}={repr(value)}')
                kwargs = ', '.join(kwargs)
            else:
                kwargs = ''

        except Exception as exc:
            result = f'\n    {type(exc).__name__}'
        print(f'{func.__name__}({args}, {kwargs}) -> {result}')
    return wrapper


'''
 16:02:33 > python -i 5.py
>>> def div_round(num1=1, num2=1, *, digits=0):
...     return round(num1 / num2, digits)
...
>>> div_round = logger(div_round)
>>> div_round(1, 3, digits=2)
div_round(1, 3, digits=2) -> 0.33
>>> div_round(5, 0, digits=0)
div_round((5, 0), {'digits': 0}) ->
    ZeroDivisionError
>>> div_round(5)
div_round(5, 1, digits=2) -> 5.0
>>> def func(*, a=0, b='\t'):
...     pass
...
>>> func = logger(func)
>>> func(a=1)
func(, a=1, b='\t') -> None
>>> def monitor(pos_key, pos_key2=2 , *, key1=None, key2=True):
...     print(f'  {pos_key=}, {pos_key2=}, {key1=}, {key2=}')
...
>>> monitor = logger(monitor)
>>> monitor(1)
  pos_key=1, pos_key2=2, key1=None, key2=True
monitor(1, 2, key1=None, key2=True) -> None
'''
