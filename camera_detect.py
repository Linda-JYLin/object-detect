import cv2
import torch
import matplotlib.pyplot as plt

# 录制
# 定义视频的编码方式、创建VideoWriter对象：参数分别是文件名、编码器、帧率、分辨率
# 注意：这里的编码器在不同操作系统上可能有所不同，'XVID'在Windows上工作良好，但在Linux上可能需要使用'mp4v'或其他
fourcc = cv2.VideoWriter_fourcc(*'XVID')


# 摄像头
cap = cv2.VideoCapture(0)
# 模型导入
model = torch.hub.load('ultralytics/yolov5','yolov5s')

ret, frame = cap.read()
print(ret)

if ret:
    # 录制参数
    width, height = frame.shape[1], frame.shape[0]
    # 创建VideoWriter对象：文件名, 编码器, 帧率, 分辨率
    out = cv2.VideoWriter("D:\yolo人脸\output.avi", fourcc, 20.0, (width, height))

    # 录制视频开始时间
    start_time = cv2.getTickCount()

    while cap.isOpened():
        ret, frame = cap.read()

        results = model(frame)
        print(results.xywh[0])

        # 框识人脸
        for result in results.xywh[0]:
            result = result
            print(result)
            x = result[0].item()
            y = result[1].item()
            w = result[2].item()
            h = result[3].item()
            if result[5] == 0:  # result[4]是阈值,result[5]是类别
                # 画矩形cv2.rectangle(image,pt1,pt2,color,thickness)
                cv2.rectangle(frame, (int(x - 1 / 2 * w), int(y - 1 / 2 * h)), (int(x + 1 / 2 * w), int(y + 1 / 2 * h)),
                              color=(0, 255, 0), thickness=3)

        # 写入帧
        out.write(frame)
        cv2.imshow('capture', frame)

        # 判断是否退出
        key = cv2.waitKey(1)
        if key &0x00FF == ord('q'):
            break

    # 释放捕获器和视频写入器
    cap.release()
    out.release()
    cv2.destroyAllWindows()

else:
    print("无法打开摄像头")
