from ctypes import windll

import win32api
import win32con
import random
import os

"""点击鼠标左键"""
def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)

"""移动鼠标到某一位置"""
def moveCurPos(x, y):
    windll.user32.SetCursorPos(x, y)

"""在指定区域内随机一个点，参数：左上角坐标，宽，高"""
def randomPosition(x, y, w, h):
    randomX = random.randint(x, x+w)
    randomY = random.randint(y, y+h)
    return randomX, randomY

"""删除文件"""
def deleteFile(filePath):
    os.remove(filePath)
