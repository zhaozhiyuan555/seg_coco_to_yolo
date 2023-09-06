import glob
import numpy as np
import json
import os
import cv2

# 根据原图和JSON格式的标签文件生成对应的YOLO的TXT标签文件保存到json_path路径下（保存文件名字和原来文件的名字一样，后缀换成txt）
json_path = r"./labelme/train2014" # 原始的JSON标签文件
TXT_path = r"./labelme/TXT_file" # 保存的TXT文件夹
image_path = r"./images/" # 原图
label_dict = {'mat': 0, 'class 2': 1, 'class 3': 2} # 类别情况
json_files = glob.glob(json_path + "/*.json")
for json_file in json_files:
    f = open(json_file)
    json_info = json.load(f)
    img = cv2.imread(os.path.join(image_path, json_info["imagePath"][0]))
    height, width, _ = img.shape
    np_w_h = np.array([[width, height]], np.int32)
    txt_file = json_file.split("\\")[-1].replace(".json", ".txt")
    txt_file = os.path.join(TXT_path, txt_file)
    f = open(txt_file, "a")
    for point_json in json_info["shapes"]:
        txt_content = ""
        np_points = np.array(point_json["points"], np.int32)
        label = point_json["label"]
        label_index = label_dict.get(label, None)
        np_points = np.array(point_json["points"], np.int32)
        norm_points = np_points / np_w_h
        norm_points_list = norm_points.tolist()
        txt_content += f"{label_index} " + " ".join([" ".join([str(cell[0]), str(cell[1])]) for cell in norm_points_list]) + "\n"
        f.write(txt_content)
 