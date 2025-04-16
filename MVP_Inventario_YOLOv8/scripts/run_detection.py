
import cv2
import os
from ultralytics import YOLO

model = YOLO('modelo/yolov8n.pt')

input_path = 'data/images'
output_path = 'data/resultados'
os.makedirs(output_path, exist_ok=True)

for img_name in os.listdir(input_path):
    img_path = os.path.join(input_path, img_name)
    img = cv2.imread(img_path)

    results = model(img)[0]
    img_result = results.plot()

    output_img_path = os.path.join(output_path, f"resultado_{img_name}")
    cv2.imwrite(output_img_path, img_result)

    print(f"Procesado: {img_name} | Guardado en {output_img_path}")
