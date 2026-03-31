import random

def create_random_matrix(rows, cols, min_val=-100, max_val=100):
    """Создаёт матрицу заданного размера со случайными целыми числами."""
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix, name=""):
    """Выводит матрицу с названием."""
    if name:
        print(f"{name}:")
    for row in matrix:
        print(row)
    print()

def sum_matrices(A, B):
    """Складывает две матрицы одинаковой размерности."""
    rows = len(A)
    cols = len(A[0]) if rows > 0 else 0
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

# Задаём размер матрицы
rows, cols = 10, 10

# Создаём две случайные матрицы
matrix_1 = create_random_matrix(rows, cols, min_val=-200, max_val=200)
matrix_2 = create_random_matrix(rows, cols, min_val=-200, max_val=200)

# Суммируем их
matrix_3 = sum_matrices(matrix_1, matrix_2)

# Выводим результат
print_matrix(matrix_1, "Матрица 1")
print_matrix(matrix_2, "Матрица 2")
print_matrix(matrix_3, "Сумма матриц (Матрица 3)")