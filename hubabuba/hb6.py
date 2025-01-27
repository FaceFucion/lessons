def find_final_position():
   # Начальная позиция
    current_position = [0, 0]

    # Считываю 5 пар координат
    for _ in range(5):
        x = int(input("Введите значение x: "))
        y = int(input("Введите значение y: "))

        # Обновляю текущую позицию
        current_position[0] += x
        current_position[1] += y

    return current_position

final_position = find_final_position()
print(f"Итоговая позиция: {final_position}")
