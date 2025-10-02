# INFO:
#Name: Zero Matrix
# Question: Write an algorithm such that if an element in a MxN matrix is 0 it's entire
# row and column are set to 0.
# Example:
# [1,2,0]
# [4,5,1]

# Solution
# [0,0,0]
# [4,5,0]

from typing import List


def zero_matrix_unoptimized_space(matrix: List[List]) -> List[List]:
    zero_row = set()
    zero_col = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
              if matrix[row][col] == 0:
                zero_row.add(row)
                zero_col.add(col)

    assert len(zero_row) == len(zero_col), "they should be the same length"

    for col, row in zip(zero_col, zero_row):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if col == j:
                    matrix[i][j] = 0
                if row == i:
                    matrix[i][j] = 0

    return matrix

#using O(1)
def zero_matrix(matrix: List[List]) -> List[List]:
    first_row_has_zero = False
    first_col_has_zero = False
    
    # have to find for first col and first row because of the overlap that occurs at point (0,0)
    for i in range(len(matrix[0])):
        if(matrix[0][i]) == 0: 
            first_row_has_zero = True
            break
    for j in range(len(matrix)):
        if(matrix[j][0]) == 0: 
            first_col_has_zero = True
            break

    #set all other heads to zero if they contain a zero
    for r in range(1,len(matrix)):
        for c in range(1,len(matrix[0])):
            if matrix[r][c] == 0: 
                matrix[0][c] = 0 
                matrix[r][0] = 0


    # nullify rows based on first column values 
    for r in range(1,len(matrix)):
        if (matrix[r][0] == 0):
            nullify_row(matrix,r)

    #nullify cols based on first row values
    for c in range(1,len(matrix[0])):
        if(matrix[0][c] == 0): 
            nullify_col(matrix,c)

    if(first_col_has_zero):
        nullify_col(matrix,0)

    if(first_row_has_zero):
        nullify_row(matrix,0)

    return matrix





def nullify_row(matrix: List[List],row_num_to_nullify) -> List[List]:
    for c in range(len(matrix[0])):
        matrix[row_num_to_nullify][c] = 0
    return matrix

def nullify_col(matrix: List[List],col_num_to_nullify) -> List[List]:
    for r in range(len(matrix)):
        matrix[r][col_num_to_nullify] = 0

    return matrix

 


if __name__ == "__main__":
    assert zero_matrix([[1, 2, 0], [4, 5, 1]]) == [
        [0, 0, 0],
        [4, 5, 0],
    ], "this is wrong"
    # Single zero in middle
    assert zero_matrix([[1, 2, 0], [4, 5, 1]]) == [
        [0, 0, 0],
        [4, 5, 0],
    ], "this is wrong"

    # No zeros
    assert zero_matrix([[1, 2, 3], [4, 5, 6]]) == [
        [1, 2, 3],
        [4, 5, 6],
    ], "this is wrong"

    # Entire row and column zeroed
    assert zero_matrix([[0, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [0, 0, 0],
        [0, 5, 6],
        [0, 8, 9],
    ], "this is wrong"

    # Multiple zeros affecting multiple rows and columns
    assert zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 0]]) == [
        [0, 0, 0],
        [4, 0, 0],
        [0, 0, 0],
    ], "this is wrong"

    # All elements already zero
    assert zero_matrix([[0, 0], [0, 0]]) == [[0, 0], [0, 0]], "this is wrong"

    # Single row matrix with zero
    assert zero_matrix([[1, 0, 3, 4]]) == [[0, 0, 0, 0]], "this is wrong"

    # Single column matrix with zero
    assert zero_matrix([[1], [0], [3]]) == [[0], [0], [0]], "this is wrong"

    # Larger matrix with scattered zeros
    assert zero_matrix(
        [[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12], [0, 14, 15, 16]]
    ) == [[0, 0, 3, 4], [0, 0, 0, 0], [0, 0, 11, 12], [0, 0, 0, 0]], "this is wrong"
