# Операции связанные  c типами последовательностями - list, tuple, range
numbers = [5, 8, 21, 57, 0, 4]
numbers_tuple = (5, 8, 21, 57, 0, 4)
numbers_range = range(0, 100)
# x находится в s
x = 21
print(x in numbers)
print(x in numbers_tuple)
print(x in numbers_range)

# x not in s
# x не находится в s
x = 33
print(x not in numbers)
print(x not in numbers_tuple)
print(x not in numbers_range)

# s + t сложение последовательностей
numbers = [5, 8, 21, 57, 0, 4]
numbers_two = [4, 0, 57, 21, 8, 5]
result = numbers + numbers_two
print(numbers + numbers_two)

numbers = (5, 8, 21, 57, 0, 4)
numbers_two = (4, 0, 57, 21, 8, 5)
result = numbers + numbers_two
print(result)

# сложение не определено на range


# s * n or n * s повторить значение s n раз
result = numbers * 3
print(result)
result = 3 * numbers
print(result)
result = "123" * 3
print(result)

# обратиться к элементу по индексу
numbers = [5, 8, 21, 57, 0, 4]
numbers_tuple = (5, 8, 21, 57, 0, 4)
numbers_range = range(0, 100)
print(numbers[2], numbers_tuple[2], numbers_range[2])

# срез значений с i по j
numbers = [5, 8, 21, 57, 0, 4]
numbers_tuple = (5, 8, 21, 57, 0, 4)
numbers_range = range(0, 100)
print(numbers[2:5])
print(numbers_tuple[2:5])
print(numbers_range[20:30])

# срез значений с i по j c шагом k
numbers = [5, 8, 21, 57, 0, 4]
numbers_tuple = (5, 8, 21, 57, 0, 4)
numbers_range = range(0, 100)
print(numbers[0:5:2])
print(numbers_tuple[0:5:2])
print(numbers_range[20:30:2])
print(numbers[::-1])
print(numbers_tuple[::-1])
print(numbers_range[::-1])

# количество значений в полседовательности
numbers = [5, 8, 21, 57, 0, 4]
numbers_tuple = (5, 8, 21, 57, 0, 4, 2)
numbers_range = range(0, 100)
print(len(numbers), len(numbers_tuple), len(numbers_range))

# Наименьший элемент в последовательности
numbers = [5, 8, 21, 57, 0, 4, -1]
numbers_tuple = (5, 8, 21, 57, 0, 4, 2)
numbers_range = range(5, 25)
print(min(numbers), min(numbers_tuple), min(numbers_range))

# Больший элемент в последовательности
numbers = [5, 8, 21, 66, 0, 4, -1]
numbers_tuple = (5, 8, 21, 57, 0, 4, 2)
numbers_range = range(5, 25)
print(max(numbers), max(numbers_tuple), max(numbers_range))

# Индекс по первому вхождению значения
numbers = [5, 8, 21, 66, 0, 4, -1]
print(numbers.index(8))

# Количество вхождений в последовательности
numbers = [5, 8, 21, 66, 8, 4, 8]
print(numbers.count(8))


# операции с изменяемыми последовательностями
numbers = [5, 8, 21, 66, 0, 4, -1]

# изменение значения элемента по индексу
numbers[2] = 23
print(numbers)

# изменение значения элемента по индексу
numbers[0:3] = [1, 2, 3]
print(numbers)

# удаление элементов по индексу/срезы
numbers = [5, 8, 21, 66, 0, 4, -1]
del numbers[0:3]
print(numbers)

# удаление элементов по индексу/срезы
numbers = [5, 8, 21, 66, 0, 4, -1]
del numbers[0]
print(numbers)

# добавление элемента в конец списка
numbers = [5, 8, 21, 66, 0, 4, -1]
numbers.append(10)
print(numbers)

#очищение списка
numbers = [5, 8, 21, 66, 0, 4, -1]
numbers.clear()
print(numbers)

#неглубокое копирование
numbers = [[5, 8, 21], [66, 0, 4], -1]
copy_numbers = numbers.copy()
print(copy_numbers)
copy_numbers[0][0] = 10
print(numbers)

#расширять список другим списком
numbers = [5, 8, 21, 66, 0, 4, -1]
numbers_extends = [5, 8, 21, 66, 0, 4, -1]
numbers.extend(numbers_extends[::-1])
print(numbers)

#вставить значение по индексу
numbers = [5, 8, 21, 66, 0, 4, -1]
numbers.insert(0, 2)
print(numbers)

#удалить значение по индексу и получить значение
numbers = [5, 8, 21, 66, 0, 4, 2]
print(numbers.pop(2))

#удалить последний элемент из списка и вернуть значение
numbers = [5, 8, 21, 66, 0, 4, 2]
print(numbers.pop())

#удаляет элемент из списка по индексу
numbers = [5, 8, 21, 66, 0, 4, 2]
numbers.remove(2)
print(numbers)

#переворачивает последовательность
numbers = [5, 8, 21, 66, 0, 4, 2]
numbers.reverse()
print(numbers)


#сортировка последовательностей
numbers = [5, 8, 21, 66, 0, 4, 2]
numbers = sorted(numbers)
print(sorted(numbers))
numbers = [5, 8, 21, 66, 0, 4, 2]
numbers.sort()
print(numbers)

#перебор массива
numbers = [5, 8, 21, 66, 0, 4, 2]
for elem in numbers:
    print(elem)


# Задание 1:
# Пользователь вводит размер списка. Список заполняется случайными значениями при помощи random.randint()
# Второй список заполнить через random.sample()
# Рандомные значения в диапазоне от 1 до 1000 включительно
# Вывести значения списка.
# Итеративно найти максимальный, минимальный элемент, среднее арифметическое, сумму значений, количество.
# Найти при помощи методов sum, max, min, среднее значение, len.
# Пользователь вводит число для поиска:
# Найти значение в списке через итерации, найти значение в списке через index
# Пользователь вводит число для поиска:
# найти количество вхождений числа итеративно и через count


# Задание 2:
# Число вводится пользователем
# Определить является ли число палиндромом (симметрично распаложены цифры в числе, например: 12344321)
# Найти сумму цифр числа


# Задание 3:
# Пользователь вводит диапзон значений x (порядок может быть любым)
# Вывести координаты x/y произвольной линейной, квадратной, кубической функций (перед коородинатами вывести формулы)
# Через библиотеку matplotlyb отрисовать графики