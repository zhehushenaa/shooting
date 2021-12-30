import threading

import time
def hu1():
    while(1):
        print("hu1")
        time.sleep(1)

def hu2():
    while(1):
        print("hu2")
        time.sleep(2)
def hu3():
    print("hu3")
    time.sleep(3)
def hu4():
    print("hu4")
    time.sleep(4)
def hu5():
    print("hu5")
    time.sleep(5)


if __name__=='__main__':
    threadList=[]

    th1 = threading.Thread(target=hu1)
    th2 = threading.Thread(target=hu2)
    th3 = threading.Thread(target=hu3)
    threadList.append(th1)
    threadList.append(th2)
    threadList.append(th3)
    for i in threadList:
        i.start()