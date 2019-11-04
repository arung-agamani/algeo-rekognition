import cv2
import pandas as pd
import numpy as np
import scipy
import pickle
import random
import os
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

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
        c = c + (int(a[i]) * int(b[i]))
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


def extract_feature(imagePath, vectorSize=64) :
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = cv2.AKAZE_create(descriptor_size=32)

    keypoints = detector.detect(image)

    keypoints = sorted(keypoints, key=lambda x: -x.response)[:vectorSize]

    keypoints, dsc = detector.compute(image, keypoints)
    

    print("keypoints : {}, descriptors : {}".format(len(keypoints), dsc.shape))

    """ cv2.drawKeypoints(image, keypoints, image, (0, 255, 0))
    cv2.imshow("Output", image)
    cv2.waitKey(0) """

    dsc = dsc.flatten()

    if dsc.size < vectorSize*64 :
        dsc = np.concatenate([dsc, np.zeros(vectorSize*64 - dsc.size)])

    return dsc

mat1 = extract_feature("nemteg.jpg")
mat2 = extract_feature("nemteg.jpg")
arr = mat1
arr2 = mat2

print("arr size : {}".format(arr.shape))
print(arr)

self_similar = CosSim(arr,arr2)
print("nemteg1 and 2 similarity : {}".format(self_similar))