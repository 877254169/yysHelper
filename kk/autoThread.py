import imgUtil
import sysUtil
import time
import os

runFlag = True
taskFlag = False

img_yuhun_start = ".\\resource\\img\\yuhun_start.png"
img_yuhun_vicotry = ".\\resource\\img\\yuhun_victory.png"
img_yuhun_wait = ".\\resource\\img\\yuhun_wait.png"
img_yuhun_end = ".\\resource\\img\\yuhun_end.png"
img_task_accept = ".\\resource\\img\\task_accept.png"
img_task_reject = ".\\resource\\img\\task_reject.png"

file_name = "tmp_yys"
file_path = ".\\resource\\tmp\\" + file_name + ".png"

def run(model, limitNum):
    # 限制次数
    if limitNum != -1:
        cnt = 1
        while runFlag and cnt <= limitNum:
            print("--------------{}--------------".format(cnt))
            if model == "御魂":
                yuhun()
            elif model == "觉醒":
                pass
            elif model == "御灵":
                pass
            elif model == "探索":
                pass
            cnt += 1
    else:
        cnt = 1
        while runFlag:
            print("--------------{}--------------".format(cnt))
            if model == "御魂":
                yuhun()
            elif model == "觉醒":
                pass
            elif model == "御灵":
                pass
            elif model == "探索":
                pass
            cnt += 1

def yuhun():
    # 先清空
    if os.path.exists(file_path):
        sysUtil.deleteFile(file_path)
    # 开始
    while runFlag:
        if yuhun_while(img_yuhun_start):
            break
    # 胜利
    while runFlag:
        if yuhun_while(img_yuhun_vicotry):
            break
        elif yuhun_while(img_yuhun_end):
            return
    # 结束
    while runFlag:
        if yuhun_while(img_yuhun_end):
            break

"""处理协作"""
def dealTask():
    if taskFlag:
        # 匹配接受
        match_res = imgUtil.match(file_path, img_task_accept)
        if match_res:
            x, y, tw, th = imgUtil.matchRange(file_path, img_task_accept)
            px, py = sysUtil.randomPosition(x, y, tw, th)
            sysUtil.moveCurPos(px, py)
            sysUtil.clickLeftCur()
            print("接受协作：({}, {})".format(px, py))
    else:
        # 匹配拒绝
        match_res = imgUtil.match(file_path, img_task_reject)
        if match_res:
            x, y, tw, th = imgUtil.matchRange(file_path, img_task_reject)
            px, py = sysUtil.randomPosition(x, y, tw, th)
            sysUtil.moveCurPos(px, py)
            sysUtil.clickLeftCur()
            print("拒绝协作：({}, {})".format(px, py))

def yuhun_while(temp_path):
    # 截图
    imgUtil.screenshot(file_name)
    # 处理协作
    dealTask()
    # 匹配
    match_res = imgUtil.match(file_path, temp_path)
    # 匹配失败则删除截图，重新开始
    if not match_res:
        sysUtil.deleteFile(file_path)
        return False
    else:
        x, y, tw, th = imgUtil.matchRange(file_path, temp_path)
        px, py = sysUtil.randomPosition(x, y, tw, th)
        sysUtil.moveCurPos(px, py)
        if temp_path == img_yuhun_end:
            time.sleep(1)
        sysUtil.clickLeftCur()
        if temp_path == img_yuhun_start:
            print("御魂-开始：({}, {})".format(px, py))
        elif temp_path == img_yuhun_vicotry:
            print("御魂-胜利：({}, {})".format(px, py))
        elif temp_path == img_yuhun_end:
            print("御魂-结束：({}, {})".format(px, py))
        return True

