class Matrix:
    def __init__(self, *args):
        self.data_matrix = []
        if isinstance(args[0], list):
            for row in args[0]:
                self.data_matrix.append([int(el) for el in row])
        elif isinstance(args[0], int) and isinstance(args[1], int):
            for j in range(args[0]):
                self.data_matrix.append([])
                for i in range(args[1]):
                    self.data_matrix[j].append(int(input(f"Введите значение {i + 1} элемента {j + 1} строки "
                                                         f"матрицы")))
        else:
            print("Заданы неподходящие параметры для определения матрицы")
            self.data_matrix = [[0]]

    def __str__(self):
        s = max([len(str(el)) for row in self.data_matrix for el in row])
        print(f"Матрица")
        return "".join([f"{''.join([f'{el}'.ljust(s + 2, ' ') for el in row])}\n" for row in self.data_matrix])

    def __add__(self, other):
        result = []
        if (len(self.data_matrix), len(self.data_matrix[0])) == (len(other.data_matrix), len(other.data_matrix[0])):
            for j in range(len(self.data_matrix)):
                result.append([])
                for i in range(len(self.data_matrix[0])):
                    result[j].append(self.data_matrix[j][i] + other.data_matrix[j][i])
            print('Суммарная', end=" ")
            return Matrix(result)
        else:
            return f'Размерность матриц не совпадает'


matrix_1 = Matrix([[1, 2], [34, 56]])
print(matrix_1)
matrix_2 = Matrix(2, 2)
print(matrix_2)
matrix_4 = matrix_1 + matrix_2
print(matrix_4)
print(matrix_2)
print(matrix_1)
matrix_3 = Matrix([[1, 2], [34, 56], [2, 4]])
print(matrix_1 + matrix_3)
