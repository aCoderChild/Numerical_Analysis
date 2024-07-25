# Find an approximation to correct to within 10-4 using the Bisection Algorithm. 25^(1/3)

import math

def f(x):
    return math.pow(x, 3) - 25

def main (f, a, b, epsilon = 1e-4, d_decimals = 10):
    i = 1
    fa = f(a)

    while True:
        p = (a + b) / 2
        fp = f(p)

        print('p' + str(i) + ' = ', round(p, d_decimals))

        if fp == 0 or (b - a) / 2 < epsilon:
            break
        elif fa * fp > 0:
            a = p
        elif fa * fp < 0:
            b = p

        i = i + 1

if __name__ == '__main__':
    a = 2
    b = 3
    main(f, a, b)

