import cv2
from Util import *

if __name__ == "__main__":
    win_handle = 68488
    win_rect = (640, 586, 1587, 1025)

    while True:
        image = GetScreenshot(win_handle, win_rect)
        cv2.imshow("ya", image)
        cv2.waitKey(1)