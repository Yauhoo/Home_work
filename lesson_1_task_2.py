#Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
number_1 = int(input('enter the first number:'))
number_2 = int(input('enter the second number:'))
number_3 = int(input('enter the last number:'))
middle = (number_3 + number_2 + number_1) / 3
print(round(middle, 3))
