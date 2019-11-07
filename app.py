import cv2
import pandas as pd
import numpy as np
import scipy
import pickle
import random
import os
import matplotlib.pyplot as plt
import collections
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
        c = c + (float(a[i]) * float(b[i]))
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

    detector = cv2.AKAZE_create()

    keypoints = detector.detect(gray)
    keypoints = sorted(keypoints, key=lambda x: x.response)[:vectorSize]

    (keypoints, dsc) = detector.compute(image, keypoints)
    if (hasattr(dsc, 'shape')) :
        print("keypoints : {}, descriptors : {}".format(len(keypoints), dsc.shape))

        dsc = dsc.flatten()

        if dsc.size < vectorSize*64 :
            dsc = np.concatenate([dsc, np.zeros(vectorSize*64 - dsc.size)])

        return dsc
    else :
        dsc = 0

    # cv2.drawKeypoints(image, keypoints, image, (0, 255, 0))
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)

    

def batch_extract(image_path):
    files = [os.path.join(image_path,p) for p in sorted(os.listdir(image_path))]

    result = {}

    for f in files:
        print("Extracting features from %s", f)
        temp = extract_feature(f)
        name = f.split('\\')[-1]
        if (type(temp) != int) :
            result[name] = temp

    print(result)
    return result

def write_db(db_obj, db_path) :
    with open(db_path, 'wb') as fp :
        pickle.dump(db_obj, fp)
        print("Database saved.")

def loadDb(db_path) :
    infile = open(db_path, 'rb')
    new_db = pickle.load(infile)
    infile.close()
    return new_db

def match(img_path, db_obj) :
    features = extract_feature(img_path)
    cont = {}
    for key in db_obj :
        cosim = CosSim(features, db_obj[key])
        cont[key] = cosim
    cont = cont.items()
    cont = sorted(cont, key=lambda kv: (kv[1], kv[0]))
    print(type(cont))
    cont.reverse()
    print(cont[:6])
    return cont

def match_euclid(img_path, db_obj) :
    features = extract_feature(img_path)
    cont = {}
    for key in db_obj :
        euclid = Euclidean(features, db_obj[key])
        cont[key] = euclid
    cont = cont.items()
    cont = sorted(cont, key=lambda kv: (kv[1], kv[0]))
    # print(type(cont))
    # print(cont[:6])
    return cont

def run():
    image_path = "db/"
    db = loadDb("extracted/features.pck")
    files = [os.path.join(image_path,p) for p in sorted(os.listdir(image_path))]

    # print(db)

    sample = random.sample(files, 1)
    # random sampling 1
    container = {}

    for s in sample :
        print("Query Image ==================")
        print(s)
        img = cv2.imread(s)
        cv2.imshow("Output", img)
        cv2.waitKey(0)
        match(s, db)

def random_sampling(image_path) :
    # db = loadDb("extracted/features.pck")
    files = [os.path.join(image_path,p) for p in sorted(os.listdir(image_path))]

    # print(db)

    sample = random.sample(files, 1)
    # random sampling 1
    container = {}
    return sample[0]