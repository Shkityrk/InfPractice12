import random


def generate_matrix():
    """
    Генерация матрицы
    :return:
    """
    matrix = [[random.randint(0, 16 * 16 - 1) for _ in range(4)] for _ in range(4)]
    return matrix
