import numpy as np
from sympy import *

a = np.array([[100, 3, 2], [6, 4, 100]])
e = Symbol("ε")
print("行列Aは\n{0}".format(a))

def one_norm(matrix):
    candidates = []
    for j in range(0,len(a[0])):
        sum = 0
        for i in range(0,len(a)):
            sum += abs(a[i][j])
        candidates.append(sum)
    matrix_norm = max(candidates)
    return matrix_norm*e

def infinity_norm(matrix):
    candidates = []
    for i in range(0,len(a)):
        sum = 0
        for j in range(0,len(a[0])):
            sum += abs(a[i][j])
        candidates.append(sum)
    matrix_norm = max(candidates)
    return matrix_norm*e

def two_norm(a):
    at = a.transpose()
    square_matrix = a.dot(at) if len(a)<=len(at) else at.dot(a)
    lambdas, v = np.linalg.eig(square_matrix)
    matrix_norm = pow(max(list(map(lambda n:abs(n), lambdas))),1/2)
    return matrix_norm*e

print("Δyの1-ノルムは{0}".format(one_norm(a)))
print("Δyの∞-ノルムは{0}".format(infinity_norm(a)))
print("Δyの2-ノルムは{0}".format(two_norm(a)))
