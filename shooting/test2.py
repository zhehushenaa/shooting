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
import cv2

import threading


from readdata.d import people


import  time


# pop=22
# poi=208
# for i in range(poi):
#     for j in range(1):
#         if image.getpixel((i, j+pop))[0]<100:
#             # print (i,j+pop)
#
#             if i-oldi>=5:
#                 ring=ring+1
#             oldi=i
#
#
#         # print (image.getpixel((i, j)))
#         # print(image.getpixel((i, j+300))[0])
#         image.putpixel((i,j+pop),pixTuple)


import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print
        "%s: %s" % (threadName, time.ctime(time.time()))




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


    print("点击位置：",event.x,event.y)
    # print("点击位置：", pox, poy)
    ttt=canvas.create_oval(event.x, event.y, event.x+1, event.y+1, fill="blue")
    # data = src_strlist[event.x, event.y]
    x.append(ttt)
    # image.putpixel((event.x, event.y), (255,20,210))




def callupdate():
    for i in x:
        # print(i)
        canvas.delete(i)



def printkey(event):
    print ("你按下了："+event.char)

def startkey():

    th.start()


def endkey():
    print ("结束！")


if __name__=='__main__':
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root,
                            width=800,  # 指定Canvas组件的宽度
                            height=600,  # 指定Canvas组件的高度
                            bg='white')  # 指定Canvas组件的背景色
    # im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片
    # image = Image.open("bg.png")
    image = Image.open('output.jpg')

    imgSize = image.size  # 大小/尺寸
    w = image.width  # 图片的宽
    h = image.height  # 图片的高
    f = image.format  # 图像格式

    print(imgSize)
    print(w, h, f)


    im = ImageTk.PhotoImage(image)
    src_strlist = image.load()

    x = []
    ring = 0
    a = 0
    dd = 0
    oldi = 0
    endbyte = 0



    th = threading.Thread(target=hustime)
    th.setDaemon(True)  # 守护线程


    pixTuple = (255, 0, 255, 15)  ###三个参数依次为R,G,B,A   R：红 G:绿 B:蓝 A:透明度
    # # A = tkinter.Button(root, text="开始", command=lambda : startkey(num=1,endbyte=endbyte))
    # A = tkinter.Button(root, text="开始", command=startkey)
    #
    # B = tkinter.Button(root, text="结束", command=endkey)
    # C = tkinter.Button(root, text="计分板", command=helloCallBack)
    # D = tkinter.Button(root, text="枪数设置", command=helloCallBack)
    # E = tkinter.Button(root, text="重置", command=callupdate)

    # A.grid()
    # B.grid()

    #A.place(x=10, y=10)
    # B.place(x=60, y=10)
    # C.place(x=60, y=10)
    # D.place(x=110, y=10)
    # E.place(x=170, y=10)

    canvas.create_image(400, 300, image=im)  # 使用create_image将图片添加到Canvas组件中
    # canvas.create_text(302, 77,  # 使用create_text方法在坐标（302，77）处绘制文字
    #                    text='标准靶'  # 所绘制文字的内容
    #                    , fill='gray')  # 所绘制文字的颜色为灰色
    # canvas.create_text(300, 75,
    #                    text='Use Canvas',
    #                    fill='blue')
    # canvas.grid()  # 将Canvas添加到主窗口

    canvas.bind("<Button -1>", callbbb)

    root.bind("<Key>", printkey)

    canvas.pack()  # 将Canvas添加到主窗口
    # image.show()

    # mypeople=people("胡深","26")
    # mypeople.readdata()



    root.mainloop()

