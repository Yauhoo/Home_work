# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
a = int(input('enter the first number:'))
b = int(input('enter the second number:'))
c = int(input('enter the last number:'))
arr = [a,b,c]
count_pos = 0
count_neg = 0
for number in arr:
    if number > 0:
         count_pos = count_pos + 1
    elif number < 0:
        count_neg = count_neg + 1
print('Negative numbers =', count_neg, "\n", 'Positive numbers =', count_pos)

