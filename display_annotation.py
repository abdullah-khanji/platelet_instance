import json
import cv2
import numpy as np
import os

# Define colors for each category
category_colors = {
    1: (255, 255, 0),# Aqua for cells
    2: (0, 255, 255), # yellow for Mito
    3: (0, 165, 255),# orange for Alpha
    4: (255, 22, 250)  # pink for Vessels
#bgr
}

# "cells":1, 
#     "Mit":2,
#     "Alpha":3,
#     "Vessels":4

def draw_annotations(image, annotations):
    """ Draw annotations on the image """
    for ann in annotations:
        category_id = ann['category_id']
        color = category_colors.get(category_id, (255, 255, 255))  # Default to white if category not found
        segmentation = ann['segmentation'][0]  # Assuming only one segmentation per annotation
        points = np.array(segmentation).reshape((-1, 2))
        points = np.int32(points)
        # Draw the polygon for segmentation as an outline
        cv2.polylines(image, [points], isClosed=True, color=color, thickness=2)
    
    return image

def visualize_annotations(json_path, image_dir, output_dir=None):
    """ Visualize annotations stored in COCO format JSON file """
    with open(json_path) as f:
        data = json.load(f)
    
    images_info = {img['id']: img for img in data['images']}
    annotations_info = data['annotations']
    
    for img_id, img_info in images_info.items():
        img_filename = os.path.join(image_dir, img_info['filename'])
        if not os.path.exists(img_filename):
            print(f"Image file {img_filename} not found.")
            continue
        
        image = cv2.imread(img_filename)
        image_annotations = [ann for ann in annotations_info if ann['image_id'] == img_id]
        
        image = draw_annotations(image, image_annotations)
        
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            output_filename = os.path.join(output_dir, img_info['filename'])
            cv2.imwrite(output_filename, image)
        else:
            cv2.imshow("Image with Annotations", image)
            cv2.waitKey(0)

    if not output_dir:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    json_path = './data/train.json'  # Path to the COCO format JSON file
    image_dir = './data/train_images/'      # Path to the directory containing original images
    output_dir = './data/visualized/'      # Directory to save visualized images (optional)

    visualize_annotations(json_path, image_dir, output_dir)
