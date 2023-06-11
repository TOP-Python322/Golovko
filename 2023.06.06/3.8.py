# ===== 8 =====

n = int(input('Введите натуральное число N\n'))
fib_numbrs = [1, 1]
i = 2
while i <= n:
    fib_numbrs.append(fib_numbrs[i-2] + fib_numbrs[i-1])
    i = i + 1
print(fib_numbrs)

'''
Введите натуральное число N
18
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
'''