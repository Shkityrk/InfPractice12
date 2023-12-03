def bubble_sort_column(matrix, col, ascending=True):
    """
    Сортировка пузырьком, в соответствии с условием вараианта
    :param matrix: <list[list[int]]>
    :param col: <int>, номер столбца
    :param ascending: <boolean>, должны ли идти элементы столбца сверху вниз в убывающем порядке, или в возрастающем
    :return: None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                condition = matrix[j][col] > matrix[j + 1][col]
            else:
                condition = matrix[j][col] < matrix[j + 1][col]

            if condition:
                matrix[j][col], matrix[j + 1][col] = matrix[j + 1][col], matrix[j][col]


def sort_columns(matrix):
    """
    Основная функция сортировки столбцов матрицы методом пузырька. Цикл осуществляет проход по всем столбцам матрицы и
    запускает сортировку в соответствии с четностью или нечетностью порядкового номера столбца.
    :param matrix: list[list[int]]
    :return: None
    """
    for col in range(4):  # учитываем, что начало отсчета в python ведется с 0, но нам нужно с 1, поэтому условия меняем
        if col % 2 == 0:
            bubble_sort_column(matrix, col, ascending=False)
        else:
            bubble_sort_column(matrix, col, ascending=True)

