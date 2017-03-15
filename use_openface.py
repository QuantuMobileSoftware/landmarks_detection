import openface
import cv2
import itertools
import os
import numpy as np

img = cv2.imread('./pics/0000000000146780.jpg', 0)

align = openface.AlignDlib('shape_predictor_68_face_landmarks.dat')

bb_roi = align.getLargestFaceBoundingBox(img)

landmarks = align.findLandmarks(img, bb_roi)

for landmark in landmarks:
    cv2.circle(img, landmark, radius=3, color=(0,0,255))

with open("output.txt", "w") as text_file:
    text_file.write("landmarks: \n {}".format(landmarks))

cv2.imwrite('result.jpg', img)
