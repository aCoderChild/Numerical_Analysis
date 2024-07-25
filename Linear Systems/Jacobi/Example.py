import numpy as np

def jacobi_iteration(A, b, x0, tol, max_iter):
    """
    Perform Jacobi iteration to solve the linear system Ax = b.

    Parameters:
    A : numpy.ndarray
        Coefficient matrix of the system.
    b : numpy.ndarray
        Right-hand side vector of the system.
    x0 : numpy.ndarray
        Initial guess for the solution vector.
    tol : float, optional
        Tolerance for convergence (default is 1e-10).
    max_iter : int, optional
        Maximum number of iterations (default is 1000).

    Returns:
    x : numpy.ndarray
        Solution vector.
    num_iters : int
        Number of iterations performed.
    """
    n = len(b)
    x = x0.copy()
    x_new = np.zeros(n)

    for iter_count in range(max_iter):
        for i in range(n):
            SUM = 0
            for j in range(n):
                if (j != i):
                    SUM = SUM + (-(A[i][j] * x[j]) / A[i][i])
            x_new[i] = SUM + b[i]/A[i][i]
        print(x)
        if np.linalg.norm(x_new - x) < tol:
            return x_new, iter_count + 1

        x = x_new.copy()

    raise RuntimeError("Jacobi iteration did not converge within the specified tolerance")

if __name__ == "__main__":
    # Example usage:
    A = np.array([[10, -1, 2, 0],
                  [-1, 11, -1, 3],
                  [2, -1, 10, -1],
                  [0, 3, -1, 8]])
    b = np.array([6, 25, -11, 15])
    x0 = np.zeros_like(b)

    tol = 1e-4
    max_iter = 1000

    solution, num_iterations = jacobi_iteration(A, b, x0, tol, max_iter)
    print("Solution:", solution)
    print("Number of iterations:", num_iterations)
