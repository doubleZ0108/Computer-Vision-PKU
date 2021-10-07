import cv2

img = cv2.imread('../../resources/opencv/card.jpg')
img = cv2.resize(img, (1000, 500))
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.namedWindow('canny')
cv2.createTrackbar('minVal', 'canny', 0, 225, lambda x: x)
cv2.createTrackbar('maxVal', 'canny', 0, 255, lambda x: x)
cv2.setTrackbarPos('minVal', 'canny', 0)
cv2.setTrackbarPos('maxVal', 'canny', 20)

while True:
    minVal, maxVal = cv2.getTrackbarPos('minVal', 'canny'), cv2.getTrackbarPos('maxVal', 'canny')
    
    # ⚠️要在gray上做才能看到效果，threshold已经滤波的差不多了根本看不出来差距
    # canny = cv2.Canny(th, minVal, maxVal)
    canny = cv2.Canny(gray, minVal, maxVal)

    cv2.imshow('canny', canny)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()