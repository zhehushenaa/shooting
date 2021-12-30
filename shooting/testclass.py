from readdata.VideoShape1 import ShapeAnalysis

import cv2 as cv
import numpy as np
import time

if __name__=='__main__':

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