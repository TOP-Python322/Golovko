def repeat(func):
    """Decorator function
    return function-wrapper, which
    repeatedly execute a called function 10 times

    """

    def wrapper(*args, **kwargs):
        for _ in range(10):
            func()
    return wrapper


def testing_function():
    """Testing function"""
    print('python')


'''
 14:15:01 > python -i 4.py
>>> testing_function = repeat(testing_function)
>>> testing_function()
python
python
python
python
python
python
python
python
python
python
'''
