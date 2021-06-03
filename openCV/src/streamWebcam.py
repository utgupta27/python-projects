import cv2 as cv

#index zero reffers to default available webcam
stream  = cv.VideoCapture(0)
while True:
    isTrue, frame = stream.read()
    cv.imshow("Webcam", frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break

stream.release()
cv.destroyAllWindows()