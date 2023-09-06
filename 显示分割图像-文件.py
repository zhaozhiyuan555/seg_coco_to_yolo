import cv2
import numpy as np
import glob
 
# 只需要给定图片文件夹和txt标签文件夹即可
pic_path = r"./images/"
txt_path = r"./labelme/TXT_file/"
 
pic = glob.glob(pic_path + "*.jpg")
 
for pic_file in pic:
    img = cv2.imread(pic_file)
    # print("***:",pic_file)
    substrings = pic_file.split('/')
    substrings = substrings[-1].split('.')
    # print("***:",substrings)
    num=substrings[0].split("\\")[1]
    height, width, _ = img.shape
    txt_file = txt_path + num + ".txt"
    file_handle = open(txt_file)
    cnt_info = file_handle.readlines()
    print("***:",cnt_info)
    new_cnt_info = [line_str.replace("\n", "").split(" ") for line_str in cnt_info]
    # print("***:",new_cnt_info)
    color_map = [(0, 255, 255), (255, 0, 255), (255, 255, 0)]
    for new_info in new_cnt_info:
        s = []
        for i in range(1, len(new_info), 2):
            b = [float(tmp) for tmp in new_info[i:i + 2]]
            s.append([int(b[0] * width), int(b[1] * height)])
        class_ = new_info[0]
        index = int(class_)
        cv2.polylines(img, [np.array(s, np.int32)], True, color_map[index], thickness = 3)
 
    save_path = 'labelme/all/' + num + '.jpg'
    # cv2.imwrite(save_path, img)
    img = cv2.resize(img, (800,416))
    cv2.imshow("{}".format(num), img)
    cv2.waitKey(0)