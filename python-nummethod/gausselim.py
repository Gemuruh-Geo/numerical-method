import numpy

#Gauss Elimination Python Sytle
def gaussElim(a,b):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if(a[i][k]!=0):
                lamp = a[i][k]/a[k][k]
                a[i][k:n] = a[i][k:n]-lamp*a[k][k:n]
                b[i] = b[i]-lamp*b[k]



# Gauss Elimination Using Looping Style
def gaussElim2(a,b):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            lamp = a[i][k] / a[k][k]
            for j in range(k,n):
                a[i][j] = a[i][j] -  lamp*a[k][j]
            b[i] = b[i] - lamp*b[k]

#Where 'a' is upper triangle matrix
def backSubstituion(a,b):
    x = [0 for i in range(0,len(b))]
    n = len(b)
    for k in range(n-1,-1,-1):
        res = numpy.dot(a[k][k+1:n],x[k+1:n])
        x[k] = (b[k]-res)/a[k][k];
    return x

def solveLinierEquationWithGaussElim(a,b):
    gaussElim(a,b)
    x = backSubstituion(a,b)
    return x
