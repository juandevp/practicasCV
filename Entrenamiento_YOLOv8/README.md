
# Entrenamiento Personalizado YOLOv8

## Requisitos
- Python 3.8+
- Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Cómo Entrenar
1. Coloca imágenes etiquetadas en:
   - `dataset/images/train/`
   - `dataset/images/val/`

2. Ejecuta entrenamiento:
```bash
python scripts/train.py
```

3. Revisa resultados en `runs/detect/modelo_personalizado2/`.

## Etiquetado de Imágenes
- [Roboflow](https://roboflow.com/).
