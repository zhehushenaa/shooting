# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# -*- cod
#
# ing:utf-8 -*-
# file: TkinterCanvas.py
#
# import tkinter  # 导入Tkinter模块
from PIL import Image, ImageTk
import tkinter.messagebox
import math


import numpy as np
import time

from readdata.VideoShape1 import ShapeAnalysis


import cv2
import threading


import cv2 as cv



import  time


import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % (threadName, time.ctime(time.time())))


def startkey(threadList):
    print ("视频流开启！")
    th = threading.Thread(target=video_capture)
    threadList.append(th)
    for a in threadList:
        if not a.is_alive():
            th.start()
            print("启动完成")


def video_capture():
    begin_time = time.time()
    start_time = begin_time
    url = 'http://192.168.1.57:81/stream'
    cap = cv.VideoCapture(url)
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv.CAP_PROP_FPS))
    print("w=", w, "h=", h, "fps=", fps)

    # 計數檢測不同frame數量
    i = 0
    f = 0
    c = 0
    amount = 0

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            src = frame
            frame = cv.resize(frame, (w * 2, h * 2), interpolation=cv.INTER_AREA)
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # imgBlur = cv.GaussianBlur(gray, (5, 5), 0)
            # ret, binary = cv.threshold(imgBlur, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

            if (time.time() - start_time) != 0:  # 实时显示帧数
                cv.putText(frame, "FPS {0}".format(float('%.1f' % (c / (time.time() - start_time)))), (5, 25),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                           1)
                # src = cv.resize(frame, (w // 2, h // 2), interpolation=cv.INTER_CUBIC)  # 窗口大小
                cv.imshow("Zoom Out", frame)
                # test print("FPS: ", c / (time.time() - start_time))
                c = 0
                start_time = time.time()

            if f == 0:
                res_old = gray
            diff = cv.subtract(gray, res_old)
            res = not np.any(diff)
            if res is False:
                # cv.imshow('DIFFERENCE', diff)
                amount = cv.countNonZero(diff)
                # test print(amount)
                # test cv.waitKey(0)
                if amount > 0:
                    diff = cv.GaussianBlur(diff, (5, 5), 0)
                    diff = cv.cvtColor(diff, cv.COLOR_GRAY2BGR)
                    # test cv.imshow('BGR', diff)

                    hsv = cv.cvtColor(diff, cv.COLOR_BGR2HSV)
                    hmin = 0
                    hmax = 180
                    smin = 0
                    smax = 43
                    vmin = 46
                    vmax = 255

                    hsv_low = np.array([hmin, smin, vmin])
                    hsv_high = np.array([hmax, smax, vmax])
                    mask = cv.inRange(hsv, hsv_low, hsv_high)
                    res = cv.bitwise_and(diff, diff, mask=mask)
                    # cv.imshow('Detect', res)
                    if f <= 2:
                        res_old = res
                        mask_old = mask

                    # 印出該色的數量
                    amount = cv.countNonZero(mask)
                    img_xor = cv.bitwise_xor(mask, mask_old)
                    amount_r = cv.countNonZero(img_xor)
                    # test print(f, "-", amount, " ", amount_r)
                    if amount_r > 0:  # 自製影片雜訊問題
                        i = i + 1
                        print("Counter=", i, " Frame=", f, " ", amount_r, " ", amount)
                        #            cv.imshow('video %s'%i, res)
                        #            cv.imshow('img %s' % f, img_xor)
                        res = cv.resize(res, (w, h), interpolation=cv.INTER_AREA)
                        ld = ShapeAnalysis()
                        px, py = ld.analysis(res)

                        cv.line(src, (px - 4, py), (px + 4, py), (0, 0, 255), thickness=2)
                        cv.line(src, (px, py - 4), (px, py + 4), (0, 0, 255), thickness=2)
                        # cv.imshow('Target', src)

                        global ttt
                        # line=0
                        #
                        # pixTuple = (255, 0, 255, 15)  ###三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
                        # oldi=0
                        # pox = event.x-13
                        # poy = event.y-92

                        # print("点击位置：",event.x,event.y)

                        px=int(px*2.5)
                        py=int(py*2.5)
                        print("点击位置：", px, py)
                        ttt = canvas1.create_oval(px, py, px + 10, py + 10, fill="blue")

                        y = py
                        realy = -4.8152 + (209.78461 / (1 + ((y / 32.21135) ** 1.3252)))
                        print(realy)

                        ccx = realy
                        ccc = -359.77681 * math.exp(-ccx / 7.79756) + 304.5269
                        print(ccc)

                        z = px
                        if z < 405:
                            q = 15 - ((405 - z) / ((405 - ccc) / 7))
                        elif z > 405:
                            q = 15 + ((z - 405) / ((405 - ccc) / 7))
                        else:
                            q = 405

                        # print(q)

                        realy = 110 + (14.5 * (39 - realy))
                        realx = 16.5 * q + 60

                        print("对应转换坐标：", str(realx), str(realy))
                        # print(realy)
                        ttt = canvas.create_oval(realx, realy, realx + 10, realy + 10, fill="blue")
                        x.append(ttt)
























            res_old = gray
            f += 1
            c += 1
        else:
            break
        k = cv.waitKey(1)
        if k == 27:
            break


    cv.waitKey(0)
    cap.release()
    cv.destroyAllWindows()


def hustime():
    while True:
        t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print (t[-2:])
        sss=canvas.create_oval(int(t[-2:])*10, int(t[-2:])*10, int(t[-2:])*10 + 10, int(t[-2:])*10+ 10, fill="blue")
        x.append(sss)

        # print ("huhuhu")
        time.sleep(5)
        # print ("   ")



def helloCallBack():
    result = tkinter.messagebox.askokcancel(title='标题~', message='内容：确认设置？')




    print(result)

def callbbb(event):
    global ttt
    line=0

    pixTuple = (255, 0, 255, 15)  ###三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
    oldi=0
    pox = event.x-13
    poy = event.y-92

    # print("点击位置：",event.x,event.y)
    print("点击位置：", pox, poy)
    ttt=canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill="blue")
    # data = src_strlist[event.x, event.y]
    x.append(ttt)
    # image.putpixel((event.x, event.y), (255,20,210))

    for i in range(pox):
        for j in range(1):
            if image.getpixel((i, j + poy))[0] < 100:
                # print(i, j + poy)

                if i - oldi >= 3:
                    line = line + 1
                oldi = i



    if line == 3:
        if poy>370:
            line = 1
    if line == 1:
        if pox > 210 and poy<150:
            line = 2
    # print (line)
    if line == 1:
        print("打中三环")

    if line == 2:
        print("打中二环")

    if line == 3:
        print("打中一环")

    if line == 4:
        print("打中二环")

    if line == 5:
        print("打中三环")


def callupdate():
    for i in x:
        # print(i)
        canvas.delete(i)



def printkey(event):
    print ("你按下了："+event.char)

# def startkey():
#
#     th.start()


def endkey():
    print ("结束！")






def callb1(event):
    global ttt
    # line=0
    #
    # pixTuple = (255, 0, 255, 15)  ###三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
    # oldi=0
    # pox = event.x-13
    # poy = event.y-92

    # print("点击位置：",event.x,event.y)
    print("点击位置：", event.x, event.y)
    ttt=canvas1.create_oval(event.x, event.y, event.x+10, event.y+10, fill="blue")

    y = event.y
    realy = -4.8152 + (209.78461 / (1 + ((y / 32.21135) ** 1.3252)))
    print(realy)

    cx = realy
    ccc = -359.77681 * math.exp(-cx / 7.79756) + 304.5269
    print(ccc)

    z = event.x
    if z < 405:
        q = 15 - ((405 - z) / ((405 - ccc) / 7))
    elif z > 405:
        q = 15 + ((z - 405) / ((405 - ccc) / 7))
    else:
        q = 405

    # print(q)

    realy = 110 + (14.5 * (39 - realy))
    realx = 16.5 * q + 60

    print("对应转换坐标：",str(realx),str(realy))
    # print(realy)
    ttt = canvas.create_oval(realx, realy, realx + 10, realy + 10, fill="blue")
    x.append(ttt)








if __name__=='__main__':

    x = []
    ring = 0
    a = 0
    threadList=[]


    root = tkinter.Toplevel()
    canvas = tkinter.Canvas(root,width=600,height=800,bg='white')
    image = Image.open('bazi.png')
    im = ImageTk.PhotoImage(image)
    # src_strlist = image.load()



    # th.setDaemon(True)  # 守护


    pixTuple = (255, 0, 255, 15)  ###三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
    A = tkinter.Button(root, text="开始", command=lambda : startkey(threadList))
    # A = tkinter.Button(root, text="开始", command=startkey)

    B = tkinter.Button(root, text="结束", command=endkey)
    C = tkinter.Button(root, text="计分板", command=helloCallBack)
    D = tkinter.Button(root, text="枪数设置", command=helloCallBack)
    E = tkinter.Button(root, text="重置", command=callupdate)


    # A.grid()
    # B.grid()
    A.place(x=10, y=10)
    B.place(x=60, y=10)
    C.place(x=60, y=10)
    D.place(x=110, y=10)
    E.place(x=170, y=10)


    canvas.create_image(300, 400, image=im)  # 使用create_image将图片添加到Canvas组件中
    canvas.bind("<Button -1>", callbbb)
    root.bind("<Key>", printkey)
    canvas.pack()  # 将Canvas添加到主窗口










    #实际打靶图
    root1 = tkinter.Toplevel()
    canvas1 = tkinter.Canvas(root1,width=800,height=600,bg='white')  # 指定Canvas组件的背景色
    image1 = Image.open('output.jpg')
    # imgSize = image1.size  # 大小/尺寸
    # w = image1.width  # 图片的宽
    # h = image1.height  # 图片的高
    # f = image1.format  # 图像格式
    # print(imgSize)
    # print(w, h, f)
    im1 = ImageTk.PhotoImage(image1)
    canvas1.create_image(400, 300, image=im1)  # 使用create_image将图片添加到Canvas组件中
    canvas1.bind("<Button -1>", callb1)
    canvas1.pack()  # 将Canvas添加到主窗口
    root1.mainloop()
    root.mainloop()




