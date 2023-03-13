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
    tl_to_br = 0
    tr_to_bl = 0

    for row in matrix:
        if matrix.index(row) == 0:
            tl_to_br += row[matrix.index(row)]
            tr_to_bl += row[len(row)-1]
        else:
            tl_to_br += row[matrix.index(row)]
            tr_to_bl += row[(matrix.index(row)*-1)-1]

    return tl_to_br + tr_to_bl