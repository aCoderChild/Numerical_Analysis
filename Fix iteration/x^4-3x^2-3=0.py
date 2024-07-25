# Use a fixed-point iteration method to determine a solution accurate to within 10^-2 for x^4 —3x^2 —3= 0 on [1, 2], Use po = 1

import math

def f(x):
    return math.pow(3 + 3 * math.pow(x, 2), 1/4)

def main (f, a, epsilon = 1e-2, d_decimals = 10):
    i = 1
    while True:
        p = f(a)
        print('p' + str(i) + ' = ', round(p, d_decimals))
        if math.fabs(p - a) < epsilon:
            break
        a = p
        i = i + 1

if __name__ == '__main__':
    a = 1
    main(f, a)