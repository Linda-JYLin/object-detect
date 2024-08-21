import cv2


def record_video(filename, duration=10):
    # 定义视频的编码方式、创建VideoWriter对象：参数分别是文件名、编码器、帧率、分辨率
    # 注意：这里的编码器在不同操作系统上可能有所不同，'XVID'在Windows上工作良好，但在Linux上可能需要使用'mp4v'或其他
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 获取摄像头的默认分辨率，或者使用自定义的分辨率
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        width, height = frame.shape[1], frame.shape[0]
        # 创建一个VideoWriter对象：文件名, 编码器, 帧率, 分辨率
        out = cv2.VideoWriter("D:\yolo人脸", fourcc, 20.0, (width, height))

        # 录制视频
        start_time = cv2.getTickCount()
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # 如果有帧，写入帧
                out.write(frame)

                # 显示结果帧
                cv2.imshow('frame', frame)

                # 按'q'键退出循环
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

                # 或者，录制特定时长的视频
        # elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
        # if elapsed_time > duration:
        #     break

        # 释放捕获器和视频写入器
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    else:
        print("无法打开摄像头")

    # 使用函数


record_video("output.avi")