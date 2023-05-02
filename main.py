import os
import cv2
import numpy as np
from PIL import ImageGrab


imgBackground = cv2.imread('resources/background.png')

#importing the mode images into a list
folderModePath = "resources/Modes"
modePathList = os.listdir(folderModePath)
imgModeList = []
print(modePathList)

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

print(len(imgModeList))


#webcam capture
# cap = cv2.VideoCapture(1)
# cap.set(3,640)
# cap.set(4,480)
# while True:
#     success, img = cap.read()
#     imgBackground[162:162+480,55:55+640]= img
#     imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]
#     #cv2.imshow("Webcam",img)
#     cv2.imshow("Face Attendance", imgBackground)
#     cv2.waitkey(1)



#screen capture version

SCREEN_SIZE = (1920, 1080) # set the screen size to match your display resolution

while True:
    # capture a screenshot of your screen
    img = np.array(ImageGrab.grab())

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert color from BGR to RGB
    img = cv2.resize(img, (640, 480)) # resize the screenshot to match the size of the area in imgBackground
    imgBackground[162:162+480, 55:55+640] = img # replace the area in imgBackground with the resized screenshot
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]
    cv2.imshow("Screen Capture", imgBackground)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
