import cv2
import face_recognition
import pickle
import os

#importing student images
folderPath = "images"
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
print(pathList)

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])
    # print(path)
    # print(os.path.splitext(path)[0])

print(studentIds)



def findEncodimgs(imagesList):
    encodeList=[]
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print("encoding started...")
encodeListKnown = findEncodimgs(imgList)
encodeListKnownWithIds = [encodeListKnown,studentIds]
print("encoding complete!")

file = open("encodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("file saved!")