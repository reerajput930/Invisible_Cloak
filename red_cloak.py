# import the file 
import cv2 as cv
import numpy as ny

# for capturing the video, 0 means camera video
cap = cv.VideoCapture(0)
# background image which u took from background.py
background = cv.imread("./background_image.jpg")


# in the loop
while True:
    # capturing the frames
    isTure, frames = cap.read()
    # this will show the non_effect video
    cv.imshow("screen",frames)
    
    # convertin bgr to hsv , as hsv is color sensetive 
    hsv = cv.cvtColor(frames,cv.COLOR_BGR2HSV)
     
    # this part is to check the hsv value of red
    # for upper bound [0,100,100] h-10
    # for lower bound [0,255,255] h+10 
    red = ny.uint8([[[0,0,255]]])#red in bgr form
    hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)#red in hsv form
   
    # lower and upper bound of red
    lower_red = ny.array([-10,100,100])
    upper_red = ny.array([10,255,255])
    
    # taking the range
    mask = cv.inRange(hsv,lower_red,upper_red)
    
    # this is part one , in which detectin the red cloak(and is for intersection part)
    mask1 = cv.bitwise_and(background,background,mask=mask)
 
    # this is part second , in which not detectin the red cloak(not for non-intersection part)
    mask= cv.bitwise_not(mask)
    mask2 = cv.bitwise_and(frames,frames,mask=mask)
    
    # merge the both part and see the magic
    cv.imshow("red_cloak",mask1+mask2)

    if cv.waitKey(5)==ord("q"):
      break

cap.release()
cv.destroyAllWindows()