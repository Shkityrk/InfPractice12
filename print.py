
def print_matrix(matrix):
    """
    Вывод матрицы
    :param matrix: list[list[int]]
    :return: None
    """
    for row in matrix:  # вывод каждой строки
        print(
            *row)  # звездочка (*) перед аргументом в контексте вывода может использоваться для распаковки элементов из итерируемого объекта.



def decimal_to_hex(matrix):
    """
    Вспомогательная функция для преобразования десятичного числа в двузначное шестнадцатеричное
    :param matrix: list[list[int]]
    :return: list[list[str]] Возвращает матрицу шестнадцатеричных значений
    """

    def decimal_to_two_digit_hex(num):
        hex_value = hex(num)[2:].upper()  # Получаем шестнадцатеричное значение и преобразуем в верхний регистр
        return hex_value.zfill(2)  # Дополняем значением '0' слева до двух символов, если необходимо

    hex_matrix = [[decimal_to_two_digit_hex(num) for num in row] for row in
                  matrix]  # Преобразование каждого элемента матрицы в шестнадцатеричное значение

    return hex_matrix
