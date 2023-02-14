def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    index = len(matrix)
    first_dia =  sum(matrix[i][i]for i in range(index))
    second_dia = sum(matrix[i][index-i-1]for i in range(index))
    print(first_dia+second_dia)

m1 = [[1,   2],[30, 40],]
m2 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
 ]
sum_up_diagonals(m2)