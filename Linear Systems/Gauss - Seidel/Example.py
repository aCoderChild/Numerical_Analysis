import numpy as np

'''
def Gauss_Seidel(A, b, x, num_steps):
    """Gauss_Seidel function takes four inputs A, a square matrix, b, the input of Ax = b, x, the initial guess, and num_steps to iterate Gauss_Seidel."""
    E = np.tril(A) 
    # np.tril: return the lower triangular matrix of A
     
    for k in range(num_steps):
        r = b - A @ x
        x = x + np.linalg.inv(E) @ r
        # inv: inverse of E
        # @: dot product
        
        print(k+1, x)
    return x  
    # return x after the loop finishes
'''
def Gauss_Seidel (A, b, x0, tol, num_steps):
    n = len(b)
    x = x0.copy()
    new_x = np.zeros(n)

    for iter_count in range(num_steps):
        for i in range(n):
            SUM = b[i] / A[i][i]
            for j in range(n):
                if(j < i):
                    SUM -= (A[i][j] * new_x[j]) / A[i][i]
                if (j > i):
                    SUM -= (A[i][j] * x[j]) / A[i][i]
            new_x[i] = SUM
        print(iter_count + 1, new_x)
        if np.linalg.norm(new_x - x) < tol:
            return new_x, iter_count + 1
        x = new_x.copy()

if __name__ == "__main__":
    # Example usage:
    A = np.array([[10, -1, 2, 0],
                  [-1, 11, -1, 3],
                  [2, -1, 10, -1],
                  [0, 3, -1, 8]])
    b = np.array([6, 25, -11, 15])
    x0 = np.zeros_like(b)

    tol = 1e-4
    num_steps = 1000

    solution = Gauss_Seidel(A, b, x0, tol, num_steps)
    print("Solution:", solution)