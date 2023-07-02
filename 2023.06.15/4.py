def repeat(func):
    # ИСПРАВИТЬ: здесь должна быть не констатация факта, а описание функциональности, которую реализует декоратор
    """Decorator function"""
    def wrapper():
        # УДАЛИТЬ: функция-обёртка не документируется
        """Wrapper function"""
        # ИСПОЛЬЗОВАТЬ: имя _ для не используемой переменной цикла
        for _ in range(10):
            func()
    return wrapper


# @repeat
def testing_function():
    """Testing function"""
    print('python')


# >>> testing_function = repeat(testing_function)
# >>> testing_function()
# python
# python
# python
# python
# python
# python
# python
# python
# python
# python

