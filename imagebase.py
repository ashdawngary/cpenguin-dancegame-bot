'''
imagebase.py
Has all core features for handling windows 10 output and screen input.
'''
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
import win32con
import win32api
import numpy
import os
import time

def getPixelatmouse():
    im = ImageGrab.grab()
    return im.getpixel(getcords())
def mousePos(cord):
    win32api.SetCursorPos(cord)

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
 
def getcords():
    return win32api.GetCursorPos()
