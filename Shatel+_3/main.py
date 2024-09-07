import cv2 as cv


cap = cv.VideoCapture(0)
face = cv.CascadeClassifier("model.xml")

while True:
    _,frame = cap.read()

    frame_Gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(frame_Gray,1.3,5)


    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        print(f"\n{x},\n{y},\n{w},\n{h}")

        f = frame[y:y+h,x:x+w]

    cv.imshow("Frame",frame)


    keys=cv.waitKey(5) & 0xff
    if(keys == 27):
        break


cv.destroyWindow()
cap.release()


