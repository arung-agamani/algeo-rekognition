# Algeo-Rekognition
Tugas Besar Algeo jilid 2 - Face Recognition using Euclidean Distance and Cosine Approximation.
Not to be confused with Amazon's Rekognition service, but you get the main idea.

# Description
AwooBot : Face Recognizer
Face recognition using euclidean distance and cosine similarity between many gradient vectors extracted from an image.
Uses OpenCV and KAZE, where the euclidean distance and cosine similarity algorithm are both hand-coded without any usage of libraries.

GUI uses Qt

# Getting Started
## Prerequisites
Before using this application, ensure that you have [Python 3](https://www.python.org/downloads/) installed, along with these required modules and packages: opencv-python, pandas, numpy, and scipy. You can download each of the modules and packages via pip (read [this](https://packaging.python.org/tutorials/installing-packages/) for more details about installing packages.)

## Using AwooBot : Face Recognizer
To run the program, open your terminal in the src folder and use python to run AwooBot.py. A dialog box would appear. The features are ready to compare your chosen image with other images in a certain database or directory.

1. You can use a prepared database or make a new one from images in one directory. To use a prepared database, simply click on 'Load Database' button and choose a database file (however, some images would not be able to be displayed after doing a match should you use a prepared database). To make a new one, click on 'Load Directory' button and choose your image directory containing the images you wanted to compare to. Make sure there are only image files in it. Afterwards, click the 'Batch Process' button and the program will start making the new database. If you want to save it, click on 'Save Database' button.
2. To choose an image you want to recognize, click on the load image and choose an image file. You can also choose a random image from a certain directory with the 'Randomize' button. Load the directory before doing so.
3. To start matching the image with the ones in the database, choose the desired method (cosine similarity or euclidean distance) and click the 'Match' button. The 'Randomize' button will also automatically do a match between the random-chosen image and the database.

Depending on your database size, the program might take some time to process.

## Testing
This program is written in **Python** using text editors. The program is tested using images from personal collection and other resources such as  [kaggle](https://www.kaggle.com/frules11/pins-face-recognition/version/1).
Each of the program features, including both of the matching methods (cosine similarity and euclidean distance), is tested to ensure that the program could run properly.

## Contributor
* 13518005 Arung Agamani Budi P.
* 13518049 Made Prisha Wulansari
* 13518098 Difa Habiba Rahman


## Ucapan Terima Kasih