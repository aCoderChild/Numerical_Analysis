#linear regression: x0 = x1

import numpy as np

def Least_Square_Method(A, b):
    AT = np.transpose(A)
    # Use @ for matrix multiplication
    A1 = np.linalg.inv(AT @ A)  # or A1 = np.linalg.pinv(AT @ A) for stability
    x = A1 @ AT @ b
    return x

if __name__ == '__main__':
    # Define A correctly as a 2D array
    A = np.array([[1, 1],
                  [1, 2],
                  [1, 3],
                  [1, 4],
                  [1, 5],
                  [1, 6],
                  [1, 7],
                  [1, 8],
                  [1, 9],
                  [1, 10]])
    # Define b correctly as a 2D array
    b = np.array([[1.3],
                  [3.5],
                  [4.2],
                  [5.0],
                  [7.0],
                  [8.8],
                  [10.1],
                  [12.5],
                  [13.0],
                  [15.6]])
    solution = Least_Square_Method(A, b)
    print("Solution:", solution.flatten())  # Flatten for easier viewing
