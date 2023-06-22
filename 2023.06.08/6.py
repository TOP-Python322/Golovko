from math import sqrt


def orth_triangle(
        cathet1: float = 0,
        cathet2: float = 0,
        hypotenuse: float = 0
) -> float | None:
    """Calculate third side of rectangular triangle on two others sides."""
    if (
            hypotenuse != 0
        and (hypotenuse < cathet1 or hypotenuse < cathet2)
         or (hypotenuse != 0 and cathet1 != 0 and cathet2 != 0)
    ):
        return None
    else:
        if hypotenuse == 0:
            hypotenuse = sqrt(cathet1 * cathet1 + cathet2 * cathet2)
            return hypotenuse
        elif cathet1 == 0:
            cathet1 = sqrt(hypotenuse * hypotenuse - cathet2 * cathet2)
            return cathet1
        elif cathet2 == 0:
            cathet2 = sqrt(hypotenuse * hypotenuse - cathet1 * cathet1)
            return cathet2
        

# >>> orth_triangle(cathet1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathet1=8, cathet2=15)
# 17.0
# >>> orth_triangle(cathet2=9, hypotenuse=3)
# None


