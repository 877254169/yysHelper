import cv2
import numpy as np
import time

img = cv2.imread(r'C:\Users\csj\Desktop\haha.png', 0)

tmp = cv2.imread(r'C:\Users\csj\Desktop\2.png', 0)

#shape是获取举证长度
print("tmp.shape =",tmp.shape)

# 获取到小图的尺寸
th, tw = tmp.shape[:2]
print("小图尺寸：h={}, w={}".format(th, tw))

t1 = time.time()
res = cv2.matchTemplate(img, tmp, cv2.TM_SQDIFF_NORMED)
t2 = time.time()
print("匹配花费时间={}".format(t2-t1))

print("res.max() = {}".format(res.max()))

#判读相似度
res2 = cv2.matchTemplate(img, tmp, cv2.TM_CCOEFF_NORMED)
print("res2.max() = {}".format(res2.max()))

# 返回匹配的最小坐标
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
tl=min_loc
print(tl)
br = (int(tl[0]) + tw, int(tl[1]) + th)
print('br==',br)
cv2.rectangle(img, tl, br, [0, 255, 0])
cv2.imshow("匹配结果" + np.str(cv2.TM_SQDIFF_NORMED), img)

cv2.waitKey(0)
cv2.destroyAllWindows()