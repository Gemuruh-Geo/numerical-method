import gausselim as gm
import numpy as np

# An n × n Vandermode matrix A is defined by
# A[i][j] =v[i]^(n−j), i=1,2,...,n, j=1,2,...,n

# v is vector
# function to create vandermode matrix


'''
[[ 1  1  1  1  1  1]
 [ 2  2  1  1  1  1]
 [ 5  3  2  1  1  1]
 [10  6  4  2  1  1]
 [18 10  5  3  1  1]
 [32 16  8  4  2  1]]
'''
def vandermode(v):
    n = len(v)
    a = np.zeros((n,n))
    for j in range(n):
        a[:,j] = v**(n-j-1)
    return a


def vandermode2(v):
    n = len(v)
    a = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a[i,j] = v[i]**(n-1-j)
    return a
v = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
a = vandermode2(v)
b = b = np.array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
x = gm.solveLinierEquationWithGaussElim(a,b)

print(x)
