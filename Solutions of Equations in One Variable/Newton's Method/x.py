# Use Newton's method to approximate, within 1e-4, the value of x that produces the point on the graph of y = x^2 that
# is closest to (1, 0)

import math

def f(x):
    return 2 * (x - 1) + 4 * math.pow(x, 3)

def f1(x):
    return 2 + 12 * math.pow(x, 2)

def main (f, f1, p0, epsilon = 1e-4):
    i = 1
    while True:
        p = p0 - f(p0) / f1(p0)
        print('p' + str(i) + ' = ' + str(p))
        if math.fabs(p - p0) < epsilon:
            break
        p0 = p
        i = i + 1

if __name__ == '__main__':
    p0 = 0.5
    main(f, f1, p0)

