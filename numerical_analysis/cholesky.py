#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math

# solve a matrix L.
def solve_L(a):
    for j in range(0,len(a)):
        sum = 0
        for k in range(0,j): ####
            sum += math.pow(a[j][k],2)
        a[j][j] = a[j][j] - sum
        if a[j][j] <= epsilon:
            print("入力した行列は非正定値")
        a[j][j] = math.sqrt(a[j][j])

        for i in range(j+1,len(A)):
            sum = 0
            for k in range(0,j-1):
                sum += a[i][k]*a[j][k]
            a[i][j] = ( a[i][j]-sum )/a[j][j]
    number_of_line = np.shape(a)[0]
    number_of_row = np.shape(a)[1]
    for i in range(0, number_of_line):
        for j in range(0, number_of_row):
            if i < j:
                a[i][j] = 0
            else:
                pass
    return a

# solve c.
def solve_c(l, b):
    c = np.arange(len(b))
    for i in range(0,len(l)):
        sum = 0
        for j in range(0,i):
            if j > i-1:
                pass
            else:
                sum = l[i][j]*c[j]
        c[i] = ( b[i]-sum )/l[i][i]
    return c

def solve_x(lt, c):
    x = np.arange(len(c))
    for i in range(0, len(lt))[::-1]:
        sum = 0
        for j in range(i+1,len(lt)):
            if j > len(lt):
                pass
            else:
                sum = lt[i][j]*x[j]
        x[i] = ( c[i]-sum )/lt[i][i]
    return x


if __name__ == "__main__":

    # initialization
    A = np.array([[4, 2], [2, 5]])
    b = np.array([2, -3])
    epsilon = 0.0

    L = solve_L(A)
    c = solve_c(L, b)
    x = solve_x(L.T, c)
    print("x = {0}, y = {1}".format(x[0],x[1]))
