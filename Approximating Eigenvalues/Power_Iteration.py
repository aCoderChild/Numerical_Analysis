import numpy as np

def p(x):
    """Compute the maximum absolute value of a vector"""
    return np.max(np.abs(x))

def power_method(n, A, x0, tol, max_iter):
    """Power Method for finding the dominant eigenvalue and eigenvector"""
    x = x0.copy()
    k = 1
    while k <= max_iter:
        y = A @ x
        yp = p(y)
        if yp == 0:
            raise ValueError("A has the eigenvalue 0, select a new vector x and restart!")
        err = p(x - y / yp)
        x = y / yp
        if err < tol:
            return yp, x
        k += 1
    return None, None  # max iterations reached

if __name__ == '__main__':
    A = np.array([[-4, 14, 0], [-5, 13, 0], [-1, 0, 2]])
    x0 = np.array([1, 1, 1])

    tol = 1e-4
    max_iter = 1000

    eigenvalue, eigenvector = power_method(3, A, x0, tol, max_iter)
    if eigenvalue is not None:
        print(f"Eigenvalue: {eigenvalue:.6f}")
        print(f"Eigenvector: {eigenvector}")
    else:
        print("Max iterations reached, no convergence.")