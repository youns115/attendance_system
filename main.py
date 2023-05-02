import cv2

#webcam recorder
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.inread('resources/background.png')

while True:
    success, img = cap.read()
    imgBackground[162:162+480,55:55+640]= img

    #cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitkey(1)