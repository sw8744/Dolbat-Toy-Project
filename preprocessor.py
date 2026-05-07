import cv2
import numpy as np

def img2rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def getSize(frame):
    h, w = frame.shape[:2]
    return w, h

def bev(frame, roi_points: list):
    w, h = getSize(frame)
    roi_points_np = np.float32([roi_points])
    dst_pts = np.float32([[0, h], [w, h], [w, 0], [0, 0]])
    matrix = cv2.getPerspectiveTransform(roi_points_np, dst_pts)
    return cv2.warpPerspective(frame, matrix, (w, h))

def gray(frame):
    h, w = frame.shape[:2]
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def mask(frame, threshold: int):
    min_white = 255 - threshold
    return cv2.inRange(frame, min_white, 255)