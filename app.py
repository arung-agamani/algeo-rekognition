# Jarak Euclidean
def Euclidean (v,w):
    n = len(v)
    c = 0
    for i in range (n):
        c += (v[i] - w[i]) ** 2
    d = c ** (1/2)
    return d
# Dot Product
def DotVectors(a, b):
    # a dan b memiliki banyak komponen sama, tidak nol
    n = len(a)
    c = 0
    for i in range(n):
        c = c + (a[i] * b[i])
    return c
# Panjang Vektor
def VectorLength(a):
    # a tidak nol
    c = 0
    n = len(a)
    for i in range(n):
        c = (a[i]**2) + c
    d = c ** 0.5
    return d
# Cosine Similarity
def CosSim(a, b):
    return DotVectors(a, b)/(VectorLength(a)*VectorLength(b))
