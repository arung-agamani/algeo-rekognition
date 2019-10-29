# Jarak Euclidean
def Euclidean (v,w):
    n = len(v)
    c = 0
    for i in range (n):
        c += (v[i] - w[i]) ** 2
    d = c ** (1/2)
    return d
