# ДОБАВИТЬ: аннотацию вызываемого объекта и возвращаемого значения
def repeat(func):
    # ИСПРАВИТЬ: здесь должна быть не констатация факта, а описание функциональности, которую реализует декоратор
    """Decorator function"""
    # ИСПРАВИТЬ: согласно условию декорируемая может принимать произвольное количество аргументов (см. тест ниже)
    def wrapper():
        # УДАЛИТЬ: функция-обёртка не документируется
        """Wrapper function"""
        # ИСПОЛЬЗОВАТЬ: имя _ для невостребованной переменной цикла
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

# >>> def msg_cleaner(text):
# ...     return text.strip()
# ...
# >>> msg_cleaner = repeat(msg_cleaner)
# >>> msg_cleaner('\tABCD\n')
# ...
# TypeError: repeat.<locals>.wrapper() takes 0 positional arguments but 1 was given


# ИТОГ: нужно лучше, доработать — 1/3
