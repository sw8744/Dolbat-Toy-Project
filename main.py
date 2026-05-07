import cv2
import numpy as np
import preprocessor
from plotter import plotROI, drawROI

ROI_POINTS = [
        [0, 480], # 좌측 아래
        [575, 480], # 우측 아래
        [475, 300], # 우측 위
        [100, 300] # 좌측 위
]

THRESHOLD = 25

# straight = preprocessor.img2rgb(cv2.imread('straight.png'))
# plotROI(ROI_POINTS, straight)

cap = cv2.VideoCapture('toy-project.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    bev_frame = preprocessor.bev(frame, ROI_POINTS)
    gray = cv2.cvtColor(bev_frame, cv2.COLOR_BGR2GRAY)
    mask_frame = preprocessor.mask(gray, THRESHOLD)

    cv2.imshow('Original', drawROI(frame, ROI_POINTS))
    cv2.imshow('BEV', bev_frame)
    cv2.imshow('Masking', mask_frame)

    if cv2.waitKey(41) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()