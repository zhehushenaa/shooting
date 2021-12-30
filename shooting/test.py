import numpy as np
import cv2

url = 'http://192.168.1.57:81/stream'

# 创建一个VideoCapture对象
cap = cv2.VideoCapture(url)

# 指定视频编解码方式为MJPG
# codec = cv2.VideoWriter_fourcc(*'MJPG')

codec = cv2.VideoWriter_fourcc(*'mp4v')

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

fps = 20.0 # 指定写入帧率为20
frameSize = (640, 480) # 指定窗口大小
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 创建 VideoWriter对象
# out = cv2.VideoWriter('video_record.avi', codec, fps, sz)


# out = cv2.VideoWriter('output.mp4', codec, fps, sz)

out = cv2.VideoWriter()
out.open('output.mp4', fourcc, fps, sz, True)

print(sz)
print("按键Q-结束视频录制")
while(cap.isOpened()):

    ret, frame = cap.read()
    # 如果帧获取正常
    if ret==True:
        # 镜像反转 flip
        # frame = cv2.flip(frame, -1)

        # 不断的向视频输出流写入帧图像
        out.write(frame)
        # 在窗口中展示画面
        cv2.imshow('frame',frame)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        print("fps=", fps)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()