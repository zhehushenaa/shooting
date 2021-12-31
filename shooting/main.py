# import tkinter  # 导入Tkinter模块
from PIL import Image, ImageTk
import tkinter.messagebox
import math
import numpy as np
from readdata.VideoShape1 import ShapeAnalysis
import threading
import cv2 as cv
import time



def startkey(threadList):
    print ("线程开始！")
    th = threading.Thread(target=video_capture)
    threadList.append(th)
    for a in threadList:
        if not a.is_alive():
            th.start()
            print("视频采集启动完成")


def video_capture():
    global plottrack
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
                        cv.imshow('Target', src)


                        px=int(px*2.5)
                        py=int(py*2.5)
                        print("点击位置：", px, py)
                        plottrack = canvas1.create_oval(px, py, px + 10, py + 10, fill="blue")

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
                            q = 0

                        # print(q)

                        realy = 110 + (16 * (39 - realy))
                        realx = 16.5 * q + 60

                        print("对应转换坐标：", str(realx), str(realy))
                        # print(realy)
                        plottrack = canvas.create_oval(realx, realy, realx + 10, realy + 10, fill="blue")
                        x.append(plottrack)

            res_old = gray
            f += 1
            c += 1
        else:
            break
        if cv.waitKey(1) == ord('q'):
            break


    cv.waitKey(0)
    cap.release()
    cv.destroyAllWindows()





def CallBack():
    result = tkinter.messagebox.askokcancel(title='标题~', message='内容：确认设置？')




    print(result)

def clickcanvas(event):
    global plottrack
    line=0

    oldi=0
    pox = event.x-13
    poy = event.y-92

    print("点击位置：", pox, poy)
    plottrack=canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="blue")

    x.append(plottrack)


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


def endkey():
    print ("结束！")






def click1(event):
    global plottrack
    print("点击位置：", event.x, event.y)
    plottrack=canvas1.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill="blue")

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

    realy = 110 + (14.5 * (39 - realy))
    realx = 16.5 * q + 60

    print("对应转换坐标：",str(realx),str(realy))
    # print(realy)
    plottrack = canvas.create_oval(realx, realy, realx + 10, realy + 10, fill="blue")
    x.append(plottrack)








if __name__=='__main__':

    x = []
    ring = 0
    a = 0
    threadList=[]


    root = tkinter.Toplevel()
    canvas = tkinter.Canvas(root,width=600,height=800,bg='white')
    image = Image.open('bazi.png')
    im = ImageTk.PhotoImage(image)

    A = tkinter.Button(root, text="开始", command=lambda : startkey(threadList))
    # A = tkinter.Button(root, text="开始", command=startkey)

    B = tkinter.Button(root, text="结束", command=endkey)
    C = tkinter.Button(root, text="计分板", command=CallBack)
    D = tkinter.Button(root, text="枪数设置", command=CallBack)
    E = tkinter.Button(root, text="重置", command=callupdate)

    # A.grid()
    # B.grid()
    A.place(x=10, y=10)
    B.place(x=60, y=10)
    C.place(x=60, y=10)
    D.place(x=110, y=10)
    E.place(x=170, y=10)

    canvas.create_image(300, 400, image=im)  # 使用create_image将图片添加到Canvas组件中
    canvas.bind("<Button -1>", clickcanvas)
    root.bind("<Key>", printkey)
    canvas.pack()  # 将Canvas添加到主窗口



    #实际打靶对照图
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
    canvas1.bind("<Button -1>", click1)
    canvas1.pack()  # 将Canvas添加到主窗口
    root1.mainloop()
    root.mainloop()




