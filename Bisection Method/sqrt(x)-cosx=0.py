#Use the Bisection method to find p3 for f(x) = sqrt(x) — cosx = 0 on [0, 1]

import math

def f(x):
    return math.sqrt(x) - math.cos(x)

def main (f, a, b, find_pn = 3):
    for i in range (1, find_pn + 1):
        fa = f(a)
        p = (a + b) / 2
        fp =f(p)

        print ('p' + str(i) + ' = ' + str(p))

        if fp == 0:
            break
        elif (fa * fp > 0):
            a = p
        elif (fa * fp < 0):
            b = p

if __name__ == '__main__':
    a = 0
    b = 1
    main(f, a, b)