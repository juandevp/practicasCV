
# MVP Inventario con YOLOv8

## Requisitos
- Python 3.8+
- Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución
- Copie imágenes en `data/images`.
- Ejecute:
```bash
python scripts/run_detection.py
```
- Resultados en `data/resultados`.

## Nota sobre el Modelo
Este MVP usa un modelo preentrenado (`yolov8n.pt`) de Ultralytics, que será reemplazado por un modelo personalizado posteriormente.
