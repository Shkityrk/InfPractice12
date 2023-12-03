def input_matrix() -> list[list[int]]:
    """
    Функция input_matrix позволяет ввести вручную каждый элемент матрицы.
    Введенные данные проверяются на принадлежность каждого элемента к алфавиту 16-ричной СС,
    а затем преобразуются в целочисленный тип 10-чной СС для корректной работы программы

    :return:matrix<list[list[int]]>
    """
    matrix = []  # matrix: list[list[int]] = []
    for i in range(4):  # цикл по строкам массива
        row = []  # объявляем массив, в котором храним данные столбца
        for j in range(4):  # цикл по каждому элементу столбца

            while True:
                try:
                    hex_number = input(f"Введите двузначное шестнадцатеричное число для [{i + 1}, {j + 1}]: ")
                    decimal_number = int(hex_number, 16)
                    while hex_number[0] == "0" and len(hex_number) != 1:
                        hex_number = hex_number[1:]

                    if (hex_number == '0') or ((0 <= decimal_number <= 16 * 16 - 1) and (len(hex_number) <= 2 and all(
                            hex_number[num] in '0123456789abcdefABCDEF' for num in range(len(hex_number))))):
                        row.append(decimal_number)
                        break
                    else:
                        print("Ошибка: Введите корректное двузначное шестнадцатеричное число.")
                except ValueError:  # Обработка ошибки неправильного вводоа числа
                    print("Ошибка: Введите корректное шестнадцатеричное число.")
        matrix.append(row)

    return matrix

