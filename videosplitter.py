import os
import numpy
import cv2


vid = cv2.VideoCapture('file path')


if not os.path.exists('images'):
    os.makedirs('images')


index = 0
while(True):

    ret, frame = vid.read()

    if not ret:
        break

    name = './images/frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)


    index += 1