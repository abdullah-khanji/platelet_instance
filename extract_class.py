from PIL import Image
import numpy as np
import os

def extract_color(image_name, color_name, lower_bound, upper_bound, output_dir, b):
    # Load the image
    image_path = os.path.join('data', b, image_name)
    print(image_path, '--------------input')
    image = Image.open(image_path)

    # Convert the image to RGB (if it's not already in that mode)
    image = image.convert('RGB')

    # Convert the image to a numpy array
    image_np = np.array(image)

    # Create a mask for the specified color
    color_mask = np.all((image_np >= lower_bound) & (image_np <= upper_bound), axis=-1)

    # Create an output image where all non-specified-color pixels are set to black
    output_image_np = np.zeros_like(image_np)  # Set background to black
    output_image_np[color_mask] = image_np[color_mask]

    # Convert the output numpy array back to an image
    output_image = Image.fromarray(output_image_np)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the output image
    output_image_path = os.path.join(output_dir, f"{image_name.split('.')[0]}.png")
    print('output:', output_image_path)
    output_image.save(output_image_path)


b='test'
if b=='train':
    # Color ranges for each class
    color_ranges = {
        "Vessels": {
            "lower": np.array([200, 200, 0], dtype=np.uint8),
            "upper": np.array([255, 255, 150], dtype=np.uint8),
            "output_dir": "./data/train_labels/Vessels/"
        },
        "Mito": {
            "lower": np.array([0, 180, 180], dtype=np.uint8),
            "upper": np.array([100, 255, 255], dtype=np.uint8),
            "output_dir": "./data/train_labels/Mito/"
        },
        "Alpha": {
            "lower": np.array([0, 100, 0], dtype=np.uint8),
            "upper": np.array([150, 255, 150], dtype=np.uint8),
            "output_dir": "./data/train_labels/Alpha/"
        }
    }

    labels = os.listdir('./data/train/')
    for image_name in labels:
        for class_name, color_info in color_ranges.items():
            extract_color(image_name, class_name, color_info["lower"], color_info["upper"], color_info["output_dir"], b)

else:
    # Color ranges for each class
    color_ranges = {
        "Vessels": {
            "lower": np.array([200, 200, 0], dtype=np.uint8),
            "upper": np.array([255, 255, 150], dtype=np.uint8),
            "output_dir": "./data/test_labels/Vessels/"
        },
        "Mito": {
            "lower": np.array([0, 180, 180], dtype=np.uint8),
            "upper": np.array([100, 255, 255], dtype=np.uint8),
            "output_dir": "./data/test_labels/Mito/"
        },
        "Alpha": {
            "lower": np.array([0, 100, 0], dtype=np.uint8),
            "upper": np.array([150, 255, 150], dtype=np.uint8),
            "output_dir": "./data/test_labels/Alpha/"
        }
    }
    labels = os.listdir('./data/test/')
    for image_name in labels:
        for class_name, color_info in color_ranges.items():
            extract_color(image_name, class_name, color_info["lower"], color_info["upper"], color_info["output_dir"], b)
    