# ===== 5 =====


from datetime import datetime as dt


def logger(func):
    """Decorator function"""
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        with open('data/function_calls.log', 'at', encoding='utf-8') as fp:
            if args == ():
                _ = [str(x) for x in func.__defaults__]
            else:
                _ = [str(x) for x in args]
            s = ', '.join(_)

            _ = []
            if kwargs == {}:
                for k, v in func.__kwdefaults__.items():
                    t = '' + k + '=' + str(v)
                    _.append(t)
            else:
                for k, v in kwargs.items():
                    t = '' + k + '=' + str(v)
                    _.append(t)
            ss = ', '.join(_)

            now = dt.now()
            now = now.strftime('%Y.%m.%d %H:%M:%S')

            try:
                result = func(*args, **kwargs)
                print(func.__name__ + '(' + s + ', ' + ss + ') -> ' + str(result))
                fp.write(now + ' — ' + func.__name__ + '(' + s + ', ' + ss + ') -> ' + str(result) + '\n')
            except Exception as ex:
                print(func.__name__ + '(' + s + ', ' + ss + ') -> \n' + type(ex).__name__)
                fp.write(now + ' — ' + func.__name__ + '(' + s + ', ' + ss + ') -> ' + type(ex).__name__ + '\n')

    return wrapper


@logger
def div_round(num1 = 1, num2 = 1, *, digits = 0):
    """Testing function"""
    return round(num1 / num2, digits) 


'''
>>> div_round(1, 3, digits=2)
div_round(1, 3, digits=2) -> 0.33
>>> div_round(7, 2)
div_round(7, 2, digits=0) -> 4.0
div_round(5, 0, digits=0) -> 
ZeroDivisionError
'''
