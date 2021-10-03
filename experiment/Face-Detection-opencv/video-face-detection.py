import cv2
from matplotlib import pyplot as plt

face_detector = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

def face_detection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    # _, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    faces = face_detector.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=19, minSize=(60, 60))
    # cv2.putText(img, '%s faces detected' % len(faces), (faces[0][0], faces[0][1]-100), cv2.FONT_HERSHEY_SIMPLEX, 2, (18,0,139), 10)
    for x, y, w, h in faces:
        cv2.rectangle(img, pt1=(x, y), pt2=(x+w, y+h), color=(18,0,139), thickness=img.shape[0]//100)

    return img

def main():
    capture = cv2.VideoCapture('video/video.MOV')

    width, height = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter('video/output.mp4', fourcc, 25, (width, height))

    if capture.isOpened():
        ret, frame = capture.read()
    else:
        ret = False

    while ret:
        detected_frame = face_detection(frame)
        writer.write(detected_frame)
        ret, frame = capture.read()

    writer.release()

if __name__ == '__main__':
    main()