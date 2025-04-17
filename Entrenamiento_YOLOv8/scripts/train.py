
from ultralytics import YOLO

# Cargar modelo YOLOv8 preentrenado
model = YOLO('yolov8n.pt')

# Entrenamiento personalizado
model.train(
    data='C:\Repos\practicasCV\Entrenamiento_YOLOv8\dataset\data.yaml',
    epochs=50,
    imgsz=640,
    batch=16,
    name='modelo_personalizado'
)
