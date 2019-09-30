from PIL import ImageGrab
import time

t1 = time.time()
im = ImageGrab.grab()
t2 = time.time()

im.save(r"test.png")
print("截图花费时间：{}".format(t2-t1))