
from ultralytics import YOLO
from matplotlib import pyplot as plt
from PIL import Image

detection_model= YOLO('yolov8n.pt')
instance_model= YOLO('yolov8n-seg.pt')

img= 'kitchen.jpg'

detection_results= detection_model.predict(img)

instance_results= instance_model.predict(img)

detection_results_array= detection_results[0].plot()
instance_results_array= instance_results[0].plot()

fig= plt.figure(figsize=(18, 9))

ax1= fig.add_subplot(1, 2, 1)
ax1.set_title("detection result")
ax1.imshow(detection_results_array)

ax2= fig.add_subplot(1, 2, 2)
ax2.set_title("Instance Results")
ax2.imshow(instance_results_array)


result= instance_results[0]

print(len(result))

box= result.boxes[0]
coords= box.xyxy[0].tolist()
class_id= box.cls[0].item()
conf= box.conf[0].item()
print("object type:", class_id)
print("Coordinates:",coords)
print("Probability: ", conf)
print(result.names)

plt.show()


