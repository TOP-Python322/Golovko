from string import ascii_uppercase, digits
from math import pow


# ОТВЕТИТЬ: неужели вручную словарь прописывали?)
# ПЕРЕИМЕНОВАТЬ: любой словарь задаёт соответствие (correspondence) — имя не несёт смысловой нагрузки — лучше явно скажите в имени, между чем и чем это соответствие
correspondence_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}


def some_to_decimal(inp_num: str, base: int) -> str | None:
    """Convert number from some numeral system to decimal system."""
    if base < 10:
        digit_list = [int(x) for x in inp_num]
        digit_list.reverse()
        # ПЕРЕИМЕНОВАТЬ: sum — это имя встроенной функции, объявляя собственную переменную с таким именем вы теряете прямой доступ к встроенной функции
        sum = 0
        n = 0
        for i in digit_list:
            sum += i * int(pow(base, n))
            n += 1
        result = str(sum)
    else:
        inp_num = inp_num.upper()
        digit_list = [x for x in inp_num]
        digit_list.reverse()
        for i in range(len(digit_list)):
            if digit_list[i] in correspondence_dict.keys():
                digit_list[i] = correspondence_dict[digit_list[i]]
        repr_digit_list = [int(x) for x in digit_list]

        sum = 0
        n = 0
        for i in repr_digit_list:
            sum += i * int(pow(base, n))
            n += 1
        result = str(sum)
    return result


def decimal_to_some(inp_num: str, base: int) -> str | None:
    """Convert number from decimal numeral system to other numeral system with some base."""
    if base < 10:
        num = int(inp_num)
        digit_list = []
        quotient = num
        while quotient >= base:
            quotient2 = int(quotient / base)
            remainder = quotient - quotient2 * base
            quotient = quotient2
            digit_list.append(remainder)

        digit_list.append(quotient)
        digit_list.reverse()
        result = [str(x) for x in digit_list]
        result = ''.join(result)
    else:
        num = int(inp_num)
        digit_list = []
        quotient = num
        while quotient >= base:
            quotient2 = int(quotient / base)
            remainder = quotient - quotient2 * base
            quotient = quotient2
            digit_list.append(remainder)

        digit_list.append(quotient)
        digit_list.reverse()
        key_list = list(correspondence_dict.keys())
        val_list = list(correspondence_dict.values())
        for i in range(len(digit_list)):
            if digit_list[i] in correspondence_dict.values():
                indx = val_list.index(digit_list[i])
                digit_list[i] = key_list[indx]

        result = [str(x) for x in digit_list]
        result = ''.join(result)
    return result


def int_base(inp_num: str, base_in: int, base_out: int) -> str | None:
    """Convert number from one numeral system to other."""
    crit1 = base_in not in range(2, 36)
    crit2 = base_out not in range(2, 36)

    crit3 = False
    ascii_exist = False
    inp_num_upper = inp_num.upper()
    for i in inp_num_upper:
        if i in ascii_uppercase:
            ascii_exist = True
            break

    if not ascii_exist:
        digit_list = [int(x) for x in inp_num]
        for i in digit_list:
            if i >= base_in:
                crit3 = True
                break
    else:
        L = [x for x in inp_num_upper]
        for i in range(len(L)):
            if L[i] in correspondence_dict.keys():
                L[i] = correspondence_dict[L[i]]
        repr_list = [int(x) for x in L]
        for i in repr_list:
            if i >= base_in:
                crit3 = True
                break

    if crit1 or crit2 or crit3:
        return None

    if base_in == 10:
        result = decimal_to_some(inp_num, base_out)
    else:
        _ = some_to_decimal(inp_num, base_in)
        result = decimal_to_some(_, base_out)

    return result


# КОММЕНТАРИЙ: очень много самоповторов и лишних действий в коде всех функций
# ИСПОЛЬЗОВАТЬ: пример более оптимального кода:

numbers_digits = dict(zip(range(36), digits + ascii_uppercase))
digits_numbers = {v: k for k, v in numbers_digits.items()}

def to_decimal(number: str, base: int) -> int | None:
    return sum(
        base**rank * digits_numbers[digit.upper()]
        for rank, digit in enumerate(number[::-1])
    )

def from_decimal(number: int, base: int) -> str:
    result = ''
    while number:
        number, remainder = divmod(number, base)
        result += numbers_digits[remainder]
    return result[::-1]

def int_base(number: str, base_from: int, base_to: int) -> str | None:
    correct_base_from = 2 <= base_from <= 36
    correct_base_to = 2 <= base_to <= 36
    correct_digits = digits_numbers[max(number).upper()] < base_from
    if not all((correct_base_from, correct_base_to, correct_digits)):
        return
    # КОММЕНТАРИЙ: для более сложных предикатов (условий) лучше не вычислять каждый по отдельности, а объединить в цепочку с помощью логических операторов — тогда вычисление следующего предиката в цепочке будет зависеть от результата в предыдущем

    number = to_decimal(number, base_from) if base_from != 10 else int(number)
    return from_decimal(number, base_to)


# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3G'
# >>> int_base('3g', 30, 2)
# '1101010'
# >>> int_base('4a', 16, 3)
# '2202'


# КОММЕНТАРИЙ: настоятельно рекомендую изучить все основные встроенные функции


# ИТОГ: поработали много и хорошо, но качество кода надо повышать
