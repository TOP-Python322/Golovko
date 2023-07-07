def check_params(func):
    """Check the correctness of function parameters"""
    def wrapper(*args, **kwargs):
        if args or len(kwargs) == 0:
            return None
        return func(**kwargs)
    return wrapper


@check_params
def orth_triangle(
        *,
        cathet1: float = 0,
        cathet2: float = 0,
        hypotenuse: float = 0
) -> float | None:
    """Calculate third side of rectangular triangle on two other sides."""
    if (
            (hypotenuse != 0 and
            (hypotenuse < cathet1 or hypotenuse < cathet2)) or
            (hypotenuse != 0 and cathet1 != 0 and cathet2 != 0) or
            (cathet1 == 0 and cathet2 == 0) or
            (cathet1 == 0 and hypotenuse == 0) or
            (cathet2 == 0 and hypotenuse == 0) or
            (cathet1 == 0 and cathet2 == 0 and hypotenuse == 0)
    ):
        return None
    else:
        if hypotenuse == 0 and cathet1 != 0 and cathet2 != 0:
            return (cathet1 ** 2 + cathet2 ** 2) ** 0.5
        elif (cathet1 == 0 or cathet2 == 0) and hypotenuse != 0:
            return (hypotenuse ** 2 - (cathet1 + cathet2) ** 2) ** 0.5


'''
 14:35:40 > python -i 6.py
>>> orth_triangle(cathet1=3, hypotenuse=5)
4.0
>>> orth_triangle(cathet1=8, cathet2=15)
17.0
>>> orth_triangle(cathet2=9, hypotenuse=3)
>>> orth_triangle(1)
>>> orth_triangle()
'''
