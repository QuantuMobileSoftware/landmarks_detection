# Landmarks detector

## Description
Program, which drawing landmarks on the biggest face on image.

Program uses:
  - OpenFace;
  - OpenCV;
  - Docker.

Program reading all images in directory "./pics" and writing them down in directory "./res_pics. File "output.txt" is storaging landmarks coordinates for each image. Example of result image is below:

![Example](https://github.com/exotikh3/landmarks_detection/blob/master/res_pics/res_0000000000146780.jpg)

## Installation

For run the program you need docker-compose.
  1. move to folder which contain project;
  2. put necessary images to folder "*/face_landmark/pics";
  3. in terminal print command "docker-compose up";
  4. get the result images in folder "*/face_landmark/res_pics".
