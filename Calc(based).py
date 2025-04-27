print("Введите первое число (целое): ", end='')
num1 = int(input())
print("Введите второе число: ", end='')
num2 = int(input())
print('Введите знак (+,-,/,*): ', end='')
sign = input()
if sign == '+':
    print("Ответ:", num1 + num2, end='')
elif sign == '-':
    print("Ответ:", num1 - num2, end='')
elif sign == '*':
    print("Ответ:", num1 * num2, end='')
elif sign == '/' and num2 != 0:
    print("Ответ:", num1 / num2, end='')
elif sign == '/' and num2 == 0:
    print('На ноль делить нельзя!', end='')
else:
    print('Неверная операция', end='')