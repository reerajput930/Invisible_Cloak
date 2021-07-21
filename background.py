import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    isTrue, background = cap.read()
    cv.imshow("screen",background)

    if cv.waitKey(5)==ord('q'):
       cv.imwrite("background_image.jpg",background)
       break

cap.release()
cv.destroyAllWindows()