from ultralytics import YOLO
from matplotlib import pyplot as plt
from PIL import Image
import yaml


model= YOLO('yolov8n-seg.yaml')
model = YOLO('yolov8n-seg.pt')

with open('./yolo_dataset/data.yaml') as stream:
    num_classes= str(yaml.safe_load(stream)['nc'])
    

print(num_classes)

project= './results/'
name='200_epochs-'
results= model.train(data='./yolo_dataset/data.yaml', project=project, name=name, epochs=200, patience=0, batch=4, imgsz=800)
