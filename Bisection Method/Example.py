# VD: tim nghiem cua phuong trinh sin(x) = 0 voi do chinh
# xac 10^-10 trong khoang [3,4]

import math

def f(x):
    return math.sin(x)

def main (f, a, b, epsilon = 1e-10, d_decimals = 10, find_pn = 10):
    pre_c = a
    for i in range (1, find_pn + 1):
        fa = f(a)
        fb = f(b)
        c = (a+b) / 2
        fc = f(c)
        print ('p' + str(i) + ' =', round(c, d_decimals))
        if fc == 0:
            break
        elif fc*fa < 0:
            b = c
        elif fc*fb < 0:
            a = c
        if math.fabs(c - pre_c) < epsilon or math.fabs((c - pre_c) / c) < epsilon:
            break
        else:
            pre_c = c

if __name__ == '__main__':
    a = 3
    b = 4
    epsilon = 1e-10
    main(f, a, b, epsilon = epsilon)