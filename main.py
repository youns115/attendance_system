import cv2
import numpy as np
from PIL import ImageGrab

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



#screen recorder

# SCREEN_SIZE = (1920, 1080) # set the screen size to match your display resolution
# FPS = 30 # set the frame rate of the video
#
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# video_writer = cv2.VideoWriter("screen_capture.mp4", fourcc, FPS, SCREEN_SIZE)
#
# imgBackground = cv2.imread('resources/background.png')
#
# while True:
#     # capture a screenshot of your screen
#     img = np.array(ImageGrab.grab())
#
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert color from BGR to RGB
#     img = cv2.resize(img, (640, 480)) # resize the screenshot to match the size of the area in imgBackground
#     imgBackground[162:162+480, 55:55+640] = img # replace the area in imgBackground with the resized screenshot
#
#     cv2.imshow("Screen Capture", imgBackground)
#     video_writer.write(imgBackground) # write the frame to the video file
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# cv2.destroyAllWindows()
# video_writer.release()

