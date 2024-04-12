import itertools


def solve_linear_equation(matrix):
    columns = [[row[n] for row in matrix] for n in range(len(matrix))]
    for column in columns:
        if column.count(0) == len(column):
            for row in matrix:
                row.remove(row[columns.index(column)])
    for row in matrix:
        if row.count(0) == len(row):
            matrix.remove(row)

    if len(matrix) >= len(matrix[0]) > 1:
        for rows_list in [list(element) for element in list(itertools.combinations(matrix, len(matrix[0]) - 1))]:
            bottom_matrix = det_matrix([row[:-1] for row in rows_list])
            if bottom_matrix != 0:
                values_list = []
                for variable in range(len(rows_list)):
                    top_matrix = det_matrix([row[:variable] + [row[-1]] + row[variable + 1:-1] for row in rows_list])
                    values_list.append([round(top_matrix / bottom_matrix, 5)])
                return values_list

    if len(matrix[0]) - len(matrix) == 1:
        bottom_matrix = det_matrix([row[:-1] for row in matrix])
        if bottom_matrix != 0:
            values_list = []
            for variable in range(len(matrix)):
                top_matrix = det_matrix([row[:variable] + [row[-1]] + row[variable + 1:-1] for row in matrix])
                values_list.append([round(top_matrix / bottom_matrix, 5)])
            return values_list
    return None


def transpose(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    return [[matrix[row_number][column_number] for row_number in range(number_of_rows)] for column_number in
            range(number_of_columns)]


def matrix_sum(matrix1, matrix2):
    number_of_rows = len(matrix1)
    number_of_columns = len(matrix1[0])
    return [[matrix1[row_number][column_number] + matrix2[row_number][column_number] for column_number in
             range(number_of_columns)] for row_number in range(number_of_rows)]


def matrix_difference(matrix1, matrix2):
    number_of_rows = len(matrix1)
    number_of_columns = len(matrix1[0])
    return [[matrix1[row_number][column_number] - matrix2[row_number][column_number] for column_number in
             range(number_of_columns)] for row_number in range(number_of_rows)]


def multiply_matrix(matrix1, matrix2):
    nrows1 = len(matrix1)
    ncolumns1 = len(matrix2)
    ncolumns2 = len(matrix2[0])
    return [[sum([matrix1[row_number][i] * matrix2[i][column_number] for i in range(ncolumns1)]) for row_number in
             range(nrows1)] for column_number in range(ncolumns2)]


def det_two_by_two_matrix(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def det_matrix(matrix):
    if not matrix:
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return det_two_by_two_matrix(matrix)
    else:
        return round(sum([((-1) ** col_number) * matrix[0][col_number] * det_matrix(
            [[matrix[r_number][n] for n in range(len(matrix[r_number])) if n != col_number] for r_number in
             range(1, len(matrix))]) for col_number in range(len(matrix))]), 5)


def inverse(matrix):
    determinant = det_matrix(matrix)
    if determinant != 0:
        index = len(matrix)
        cofactor_matrix = [[((-1) ** (column_number + row_number)) * det_matrix(
            [[matrix[r_number][n] for n in range(len(matrix)) if n != column_number] for r_number in range(len(matrix))
             if r_number != row_number]) for column_number in range(index)] for row_number in range(index)]
        adjoint_matrix = transpose(cofactor_matrix)
        inverse_matrix = [[round(value / determinant, 3) for value in row] for row in adjoint_matrix]
        return inverse_matrix
    elif determinant == 0:
        return None


def matrix_from_dict(canvas):
    return [[float(canvas.dict[f"Row {i} Column {j}"]['Variable'].get()) if
             canvas.dict[f"Row {i} Column {j}"]['Variable'].get().replace(".", "").replace("-", "").isdigit() else 0 for
             j in range(canvas.number_of_columns.get())] for i in range(canvas.number_of_rows.get())]
