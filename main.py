import sys, math

# Базовые операции с числами, строками и списками

# Логические операторы
# x or  y - логическая операция или
# x and y - логическая операция и
# not x  -  логическая операция не

#логические выражения
# < - меньше
# <= меньше или равно
# > - больше
# >= - больше или равно
# == равно
# != не равно
# is ссылаются ли объекты на одно значение
# is no

#арифмитические выражения над числами
x, y  = -5, 7
print(x+y) #сложение
print(x-y) #вычитание
print(x*y) #умножение
print(x/y) #деление, результат деления всегда число типа данных float
print(x//y) #деление нацело, округление всегда в нижнюю сторону
print(x%y) #остаток от деления
print(-x) #смена знака на противоположный
print(+x) #знак не остается прежним
print(abs(x)) #модуль значения
print(int(x)) #преобразовать в int
print(float(x)) #преобразовать в float
print(divmod(x, y)) #целочисленное деление и остаток от деления (возвращается кортежем)
print(pow(x, y)) #возвести х в степень у
print(x ** y) #возвести х в степень у

#часть математических операций
print(math.trunc(4.24)) #отсечение дробной части
print(round(1.256256, 5)) #округление числа до n знака
print(math.floor(1.51)) #округление вниз
print(math.ceil(1.51)) #округление вверх

#Задание 1
#приоритеты операций https://docs.python.org/3/reference/expressions.html#operator-summary
#считать с консоли input(), вывести в консоль print()

#Вычислить выражения:
#((a+b)^2 - 4bc + 10)/11 ответ преобразовать в целое число
#ab + ac*(-b) / a*c^2 найти целое и остаток деления этого выражения на 4
#|a^2 - c^2 - b^2|/256.432 - точность до двух знаков после запятой

#Задание 2
#Сотавить таблицу истиности двух переменных для следующих выражений
#x или y,x и y, не (x или y), не (x и y), x исключающая или y
#не х, не y
#таблицу вывести в формате:
#x  y   (x и y) (x или у) не (x и y)
#0  0   0        0        1
#и тд