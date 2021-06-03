import cv2 as cv

def rescaleFrame(frame,scale = 0.50):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    return cv.resize(frame,(width, height),interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('/home/utgupta27/PycharmProjects/python-projects/openCV/videos/dogs.mp4')
while True:
    isTrue, frame = capture.read()
    frame = rescaleFrame(frame,0.25)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break

capture.release()
cv.destroyAllWindows()