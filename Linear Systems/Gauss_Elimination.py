import numpy as np

def Gauss_Elimination(a_matrix, b_matrix):
    # Adding some contingencies to prevent future problems
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Error: Square matrix not given")
        return

    if b_matrix.shape[1] != 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("Error: constant vector incorrectly sized")
        return

    # Initialization of necessary variables
    n = len(b_matrix)
    x = np.zeros(n)
    new_line = "\n"

    # Create our augmented matrix through numpy's concatenate feature
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis=1)
    print(f"The initial augmented matrix is: {new_line}{augmented_matrix}")
    print("Solving for the upper triangular matrix:")

    # Applying Gauss Elimination
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented_matrix[k][i]) > abs(augmented_matrix[max_row][i]):
                max_row = k

        # Swap the current row with the max row
        if max_row != i:
            augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]

        for j in range(i + 1, n):
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - (scaling_factor * augmented_matrix[i])

        print(augmented_matrix)  # For visualizing the process

    # Backward substitution
    x[n - 1] = augmented_matrix[n - 1][n] / augmented_matrix[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = augmented_matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= augmented_matrix[i][j] * x[j]
        x[i] /= augmented_matrix[i][i]

    # Displaying solution
    print("The following x_vector matrix solves the above augmented matrix: ")
    for answer in range(n):
        print(f"x{answer} is {x[answer]}")

    return x


if __name__ == '__main__':
    variable_matrix = np.array([[1, -1, 2, -1], [2, -2, 3, -3], [1, 1, 1, 0], [1, -1, 4, 3]], dtype=float)
    constant_matrix = np.array([[-8], [-20], [-2], [4]], dtype=float)
    solution = Gauss_Elimination(variable_matrix, constant_matrix)
    print("Solution:", solution)
