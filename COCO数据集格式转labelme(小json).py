import json
import os

def coco_to_labelme(coco_file, output_dir):
    with open(coco_file, 'r') as f:
        data = json.load(f)

    images = data['images']
    annotations = data['annotations']
    categories = {category['id']: category['name'] for category in data['categories']}

    for image in images:
        image_id = image['id']
        image_file = image['file_name']
        print(image['file_name'].rsplit('\\', 1))
        # dir, image_file_1 = image['file_name'].rsplit('\\', 1) # 如果包含路径则需要通过这种方式获取文件名
        image_file_1 = image['file_name'].rsplit('\\', 1)
        image_width = image['width']
        image_height = image['height']

        labelme_data = {
            "version": "5.0.1",
            "flags": {},
            "shapes": [],
            "imagePath": image_file_1,
            "imageData": None,
            "imageHeight": image_height,
            "imageWidth": image_width
        }

        for annotation in annotations:
            if annotation['image_id'] == image_id:
                category_id = annotation['category_id']
                category_name = categories[category_id]
                bbox = annotation['bbox']
                segmentation = annotation['segmentation'][0]

                # Convert segmentation to polygon format
                polygon = []
                for i in range(0, len(segmentation), 2):
                    x = segmentation[i]
                    y = segmentation[i + 1]
                    polygon.append([x, y])

                shape_data = {
                    "label": category_name,
                    "points": polygon,
                    "group_id": None,
                    "shape_type": "polygon",
                    "flags": {}
                }

                labelme_data['shapes'].append(shape_data)

        image_name = os.path.splitext(os.path.basename(image_file))[0]
        labelme_output_file = os.path.join(output_dir, image_name + '.json')

        with open(labelme_output_file, 'w') as f:
            json.dump(labelme_data, f, indent=4)

        print(f"Converted {image_file} to {labelme_output_file}")

# 使用示例
coco_file = r'annotations/instances_train2014.json'
output_dir = r'labelme/train2014'

coco_to_labelme(coco_file, output_dir)
