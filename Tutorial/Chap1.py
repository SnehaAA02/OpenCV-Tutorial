import cv2


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480) 

#cap=cv2.VideoCapture("Resources/video.mp4")
while True:
    success,img=cap.read()      #return bool video(whether successfull) and stores img
    cv2.imshow("Video",img)
    if cv2.waitKey(1)  & 0XFF ==ord('q'):
       break