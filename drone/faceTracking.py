from utlis import *
import cv2

w,h = 360,240
pid = [0.4,0.4,0]
pError = 0
startCounter = 0
myDrone = initializeTello()

while True:

    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1

    img = telloGetFrame(myDrone,w,h)
    img, info = findFace(img)
    pError = trackFace(myDrone,info,w,pid,pError)

    cv2.imshow('Image',img)
    if cv2.waitKey(1):
        myDrone.land()
        break