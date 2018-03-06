import gausselim as gm
import numpy as np
a = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]],float)
b = np.array([11,-16,17],float)

c = gm.solveLinierEquationWithGaussElim(a,b)
print(c)
