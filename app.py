import cv2
import pandas as pd
import numpy as np
import scipy
import pickle
import random
import os
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

def extract_feature(imagePath, vector_size=32) :
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = cv2.AKAZE_create()
    (kps, dsc) = detector.detectAndCompute(gray, None)
    print("keypoints : {}, descriptors : {}".format(len(kps), dsc.shape))

    cv2.drawKeypoints(image, kps, image, (0, 255, 0))
    cv2.imshow("Output", image)
    cv2.waitKey(0)

    return dsc

mat1 = extract_feature("0.jpg")
arr = np.hstack(mat1)

print("arr size : {}".format(arr.shape))
print(arr)

self_similar = cosine_similarity(arr)



