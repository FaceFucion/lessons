# Считываю числа a и b с клавиатуры
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Нахожу все числа в диапазоне [a; b], которые кратны 3
sum_of_numbers = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0:  # Проверяю кратность 3
        sum_of_numbers += i
        count += 1

# Вычисляю среднее арифметическое
average = sum_of_numbers / count

# Вывожу результат
print(f"Среднее арифметическое чисел, кратных 3, на отрезке [{a}; {b}]: {average}")
