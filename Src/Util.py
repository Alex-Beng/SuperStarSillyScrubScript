import cv2
import os
import datetime
import win32gui, win32ui, win32con, win32api
from ctypes import windll
import numpy
import base64
from PIL import Image

DEBUGING = True
# DEBUGING = False

def SHOW_IMAGE(image):
    if DEBUGING:
        now = datetime.datetime.now()
        now = str(now)
        cv2.imshow(now, image)
        cv2.waitKey()
        cv2.destroyWindow(now)
    else:
        pass

# 需手动获取窗口曲柄&Rect
def GetScreenshot(win_handle, win_rect):
    hWnd = win_handle
    left, top, right, bot = win_rect
    width = right - left
    height = bot - top

    hWndDC = win32gui.GetWindowDC(hWnd)
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)
    signedIntsArray = saveBitMap.GetBitmapBits(True)

    im_opencv = numpy.frombuffer(signedIntsArray, dtype = 'uint8')
    im_opencv.shape = (height, width, 4)
    cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2RGB)
    
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd,hWndDC)

    return im_opencv
def GetScreenshotByAdb():
    os.system('adb shell screencap -p /sdcard/temp.png')
    os.system('adb pull /sdcard/temp.png ../Pics/')
    image = cv2.imread("../Pics/temp.png")
    image = cv2.resize(image, (image.shape[0]//2, image.shape[1]//2))
    return image
