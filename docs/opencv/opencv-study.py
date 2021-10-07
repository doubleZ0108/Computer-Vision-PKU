import cv2
import numpy as np
import matplotlib.pyplot as plt

def call_back_func(x):
    print(x)


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

img = cv2.imread("../resources/lena.jpg")
cv2.namedWindow('image')
cv2.createTrackbar('attr', 'image', 0, 255, call_back_func)
while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break
    
    # attr = cv2.getTrackbarPos('attr', 'image')
    # img[:] = [attr, attr, attr]

    cv2.setMouseCallback('image', mouse_event)


###
