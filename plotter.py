import cv2
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

def plotROI(roi_points: list, img):
    x = []
    y = []
    for point in roi_points:
        x.append(point[0])
        y.append(point[1])

    plt.imshow(img)
    plt.title('ROI')
    plt.scatter(x, y, color='red', s=50)

    x.append(roi_points[0][0])
    y.append(roi_points[0][1])

    plt.plot(x, y, color='red')
    plt.show()

def drawROI(frame, roi_points):
    cv2.line(frame, roi_points[0], roi_points[1], (0, 0, 255), 3)
    cv2.line(frame, roi_points[1], roi_points[2], (0, 0, 255), 3)
    cv2.line(frame, roi_points[2], roi_points[3], (0, 0, 255), 3)
    cv2.line(frame, roi_points[3], roi_points[0], (0, 0, 255), 3)
    
    return frame