a2 = int(input("Введите десятки первого числа (a2): "))
a1 = int(input("Введите единицы первого числа (a1): "))
b = int(input("Введите однозначное число (b): "))
num1 = a2 * 10 + a1
num2 = b
summa = num1 + num2
sum_a2 = summa // 10
sum_a1 = summa % 10
num3 = a2*10 + a1 + b
print("Цифра десятков суммы:", sum_a2)
print("Цифра единиц суммы:", sum_a1)
print("Число:", num3)
