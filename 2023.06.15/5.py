def logger(func):
    # ИСПРАВИТЬ: здесь должна быть не констатация факта, а описание функциональности, которую реализует декоратор
    """Decorator function"""
    def wrapper(*args, **kwargs):
        # УДАЛИТЬ: функция-обёртка не документируется
        """Wrapper function"""
        if args == ():
            # ИСПОЛЬЗОВАТЬ: имя _ не должно применяться вместо значащих имён переменных
            args_ = [str(x) for x in func.__defaults__]
        else:
            args_ = [str(x) for x in args]
        # ПЕРЕИМЕНОВАТЬ: используйте то же имя args_
        s = ', '.join(args_)

        kwargs_ = []
        if kwargs == {}:
            for k, v in func.__kwdefaults__.items():
                # ПЕРЕИМЕНОВАТЬ: что означает t?
                t = '' + k + '=' + str(v)
                kwargs_.append(t)
        else:
            for k, v in kwargs.items():
                t = '' + k + '=' + str(v)
                kwargs_.append(t)
        # ПЕРЕИМЕНОВАТЬ: используйте то же имя kwargs_
        ss = ', '.join(kwargs_)

        try:
            result = func(*args, **kwargs)
            print(func.__name__ + '(' + s + ', ' + ss + ') -> ' + str(result))
        except Exception as ex:
            print(func.__name__ + '(' + s + ', ' + ss + ') -> \n' + type(ex).__name__)

    return wrapper


# @logger
def div_round(num1=1, num2=1, *, digits=0):
    """Testing function"""
    return round(num1 / num2, digits) 


# >>> div_round(1, 3, digits=2)
# div_round(1, 3, digits=2) -> 0.33

# >>> div_round(7, 2)
# div_round(7, 2, digits=0) -> 4.0

# div_round(5, 0, digits=0) ->
# ZeroDivisionError


# КОММЕНТАРИЙ: с кодом, оформленным так, как вы пишете уже которое задание подряд, вы не пройдёте ни одно техническое собеседование, даже если алгоритмически код будет безупречен (а до этого пока весьма далеко) — специалисты, регулярно просматривающие десятки ответов кандидатов, ваш ответ выкинут только взглянув, потому что на его чтение надо потратить в два–четыре раза больше сил и времени — это никому не интересно

