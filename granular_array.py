"""
Dado un array 1D que tiene una cantidad enorme de entradas,
por ejemplo demasiado grande como para poder graficar en un heatmap,
obtener un array 1D nuevo como resultado de promediar el array
original "de a cachos".
"""
#  Chunking function 
def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

# Resampling function
def resample(arr, newLength):
    chunkSize = len(arr)/newLength
    return [np.mean(chunk) for chunk in chunks(arr, chunkSize)]

"""
Example:
import numpy as np
x = np.linspace(-1,1,15)
y = resample(x, 5)
print y
# Result:
# [-0.85714285714285721, -0.4285714285714286, -3.7007434154171883e-17, 0.42857142857142844, 0.8571428571428571]
"""