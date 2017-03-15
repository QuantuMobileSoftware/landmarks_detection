import openface
import cv2
import itertools
import os
import numpy as np



align = openface.AlignDlib('shape_predictor_68_face_landmarks.dat')

with open("output.txt", "w") as text_file:
    for filename in os.listdir('./pics'):
        img = cv2.imread('./pics/'+filename, 0)

        bb_roi = align.getLargestFaceBoundingBox(img)

        landmarks = align.findLandmarks(img, bb_roi)

        for landmark in landmarks:
            cv2.circle(img, landmark, radius=3, color=(0,0,255))

        text_file.write("landmarks  {}: \n {} \n\n".format(filename, landmarks))
        cv2.imwrite('./res_pics/res_'+filename, img)
