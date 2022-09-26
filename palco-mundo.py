import numpy as np
import cv2

VIDEO = 'D:/MEI/Portfólio/background-remove/PisaTimelapse.mp4'


cap = cv2.VideoCapture(VIDEO)

framesIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)
#print(framesIds)

frames = []
for fid in framesIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    hasFrame, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    frames.append(frame)
    


medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
#print(medianFrame)
cv2.imshow('Frame 1', frames[1])
cv2.imshow('Median frame', medianFrame)
cv2.waitKey(0)
cv2.imwrite('median_frame-pisa.jpg', medianFrame)
