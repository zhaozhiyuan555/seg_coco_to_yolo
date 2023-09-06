import cv2
import numpy as np

# 只需要给定图片和txt标签文件即可（单独的）
pic_path = r"./images/2023060111212345_11.jpg"
txt_path = r"./labelme/TXT_file/2023060111212345_11.txt"
 
img = cv2.imread(pic_path)
img0 = img.copy()
height, width, _ = img.shape
 
file_handle = open(txt_path)
cnt_info = file_handle.readlines()
new_cnt_info = [line_str.replace("\n", "").split(" ") for line_str in cnt_info]
 
color_map = [(0, 255, 255), (255, 0, 255), (255, 255, 0)]
for new_info in new_cnt_info:
    s = []
    for i in range(1, len(new_info), 2):
        b = [float(tmp) for tmp in new_info[i:i + 2]]
        s.append([int(b[0] * width), int(b[1] * height)])
    class_ = new_info[0]
    index = int(class_)
    cv2.polylines(img, [np.array(s, np.int32)], True, color_map[index], thickness = 3)

img = cv2.resize(img, (800,416))
img0 = cv2.resize(img0, (800,416))

cv2.imshow('ori', img0)
cv2.imshow('result', img)
cv2.waitKey(0)