# INFO:
# Question: Rotate Matrix(rotation clockwise)
# Description: Given an image represented by a NxN matrix, where each pixel in the image
# is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

from typing import List


def rotate_matrix_my_version(matrix: List[List]) -> List[List]:
    # 🚧this solution is wrong and is me thinking I was right but it turns out it only worked for the solution I was trying to do
    # although I somehow landed on the same answer that I was supposed to somehow
    # rotation of matrix is pertaining to clockwise rotation
    # for each x & y coordinate for a row, swictch x and y and then reverse that list
    # solution with another data structure
    # NOTES: I landed on the algorithm accidentally somehow I don't know how though I think I might have done something wrong somwehre
    assert len(matrix) == len(matrix[0]), "the matrix should be a square matrix"
    matrix_length = len(matrix)
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    coordinates = []
    for i in range(matrix_length):
        row_coordinates = []
        for j in range(matrix_length):
            row_coordinates.append((j, i))
        coordinates.append(row_coordinates)

    for i in range(len(coordinates)):
        coordinates[i] = coordinates[i][::-1]
    print(coordinates)

    print(new_matrix)
    for i in range(matrix_length):
        for j in range(matrix_length):
            x = coordinates[i][j][0]
            y = coordinates[i][j][1]
            print("value at position", new_matrix[x][y])

            print("x", x)
            print("y", y)

            new_matrix[x][y] = matrix[i][j]
            print("new matrix", new_matrix)

    print(new_matrix)

    return new_matrix


def rotate_matrix(matrix: List[List]) -> List[List]:
    # from what I discovered my self thank God it's the same as finding transpose and then reversing the lists
    assert len(matrix) == len(matrix[0]), "the matrix should be a square matrix"
    matrix_length = len(matrix)

    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

    for i in range(matrix_length):
        matrix[i] = matrix[i][::-1]

    print(matrix)

    return matrix


if __name__ == "__main__":
    # Test case 1: 3x3 matrix (updated for clockwise rotation)
    assert rotate_matrix([[1, 2, 3], [1, 2, 4], [1, 3, 4]]) == [
        [1, 1, 1],
        [3, 2, 2],
        [4, 4, 3],
    ], "Failed to rotate 3x3 matrix clockwise correctly"

    # Test case 2: 1x1 matrix (single element, unchanged as rotation doesn't affect 1x1)
    assert rotate_matrix([[5]]) == [[5]], "Failed to rotate 1x1 matrix correctly"

    # Test case 3: 2x2 matrix (updated for clockwise rotation)
    assert rotate_matrix([[1, 2], [3, 4]]) == [
        [3, 1],
        [4, 2],
    ], "Failed to rotate 2x2 matrix clockwise correctly"

    # Test case 4: 4x4 matrix (updated for clockwise rotation)
    assert rotate_matrix(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    ) == [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ], "Failed to rotate 4x4 matrix clockwise correctly"

    # Test case 5: Matrix with negative numbers (updated for clockwise rotation)
    assert rotate_matrix([[0, -1], [-2, -3]]) == [
        [-2, 0],
        [-3, -1],
    ], "Failed to rotate matrix with negative numbers clockwise"

    # Test case 6: Matrix with duplicate values (updated for clockwise rotation)
    assert rotate_matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == [
        [3, 2, 1],
        [3, 2, 1],
        [3, 2, 1],
    ], "Failed to rotate matrix with duplicate values clockwise"
