import os
import cv2
import pickle
import face_recognition

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

folderModePath = "Resources/Modes"
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Load the encoding file
print("Loading encode file...")

file = open('Encode File.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()

encodeListKnown, studentIds = encodeListKnownWithIds

print("Encode file loaded.")

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162: 162 + 480, 55: 55 + 640] = img  # Overlay the camera output over graphics
    imgBackground[44: 44 + 633, 808: 808 + 414] = imgModeList[0]  # Overlay the mode over graphics

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        print("Matches", matches)
        print("Face Distance", faceDis)

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
