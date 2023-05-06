import cv2
#from deepface import DeepFace
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img=cv2.imread("D:\OpenCv\Resources\happygirl.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces =faceCascade.detectMultiScale(imgGray,1.1,4)  #to find faces
for(x,y,w,h) in faces:            #rect around face
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result",img)
cv2.waitKey(0)