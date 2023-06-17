# ===== 4 =====


def repeat(func):
    """Decorator function"""
    def wrapper():
        """Wrapper function"""
        for i in range(10):
            func()
    return wrapper


# @repeat
def testing_function():
    """Testing function"""
    print('python')


'''
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
