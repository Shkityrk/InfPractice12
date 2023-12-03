import random  # Импорт модуля random для генерации случайных чисел
import sys  # Импорт модуля sys для взаимодействия с интерпретатором Python

from generate import generate_matrix
from input import input_matrix
from sort import sort_columns
from print import print_matrix, decimal_to_hex


def main():
    while True:
        choice = input(
            "Выберите способ заполнения матрицы (1 - ввести вручную, 2 - сгенерировать, q - выход): ")  # выбор варианта работы

        if choice == 'q':  # Завершение работы программы
            sys.exit(0)
        elif choice == '1':  # Ввод матрицы вручную
            matrix = input_matrix()
        elif choice == '2':  # Генерация матрицы
            matrix = generate_matrix()
        else:  # Ошибка
            print("Некорректный выбор. Введите 1, 2 или q.")
            continue

        print("Исходная матрица:")
        print_matrix(decimal_to_hex(matrix))  # Вывод исходной матрицы

        sort_columns(matrix)  # Сортировка столбцов
        hex_matrix = decimal_to_hex(matrix)  # Преобразование матрицы в 16-ную СС

        print("\nМатрица после сортировки:")
        print_matrix(hex_matrix)  # Вывод отсортированной матрицы


if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:  # Обработка ошибки закрытия программы через Ctrl+C
            print("\n\nВсе попытки меня сломать обернутся неудачей :)\nТеперь все придется начинать сначала😊\n\n")
            continue
        except Exception as e:  # Обработка остальных ошибок
            print(f" Произошла ошибка: {e}")
