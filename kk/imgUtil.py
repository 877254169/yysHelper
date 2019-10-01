import time

from PIL import ImageGrab
from ctypes import windll
import cv2

"""截屏需要的相关信息"""
user32 = windll.user32
user32.SetProcessDPIAware()

"""截全屏并保存"""
def screenshot(filename):
    img = ImageGrab.grab()
    filepath = r".\\resource\\tmp\\" + filename + ".png"
    img.save(filepath)

"""在img中匹配图片template，当相似度>0.97时，返回true"""
def match(img_path, template_path):
    img = cv2.imread(img_path, 0)
    template = cv2.imread(template_path, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    if res.max() > 0.97:
        print("match = {}".format(res.max()))
        return True
    else:
        return False

"""返回在img中template匹配到的左上角坐标和template宽高"""
def matchRange(img_path, template_path):
    img = cv2.imread(img_path, 0)
    template = cv2.imread(template_path, 0)
    # res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    th, tw = template.shape[:2]
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # return min_loc[0], min_loc[1], tw, th
    return max_loc[0], max_loc[1], tw, th # 匹配策略不是 TM_SQDIFF_NORMED 时用这个