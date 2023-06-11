# ===== 1 =====


print("Введите числа кратные семи")
nums = []
while True:
    num = int(input())
    if num % 7 == 0:
        nums.append(num)
    else:
        break
length = len(nums)
output = '' 
for i in range(length):
    output += str(nums[length - i - 1]) + ' '
print(output)


'''
Введите числа кратные семи
7
14
42
49
4
49 42 14 7
'''