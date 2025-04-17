# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 21:21:13 2025

@author: juanc
"""
from ultralytics import YOLO

model = YOLO('C:/Repos/practicasCV/Entrenamiento_YOLOv8/dataset/runs/detect/modelo_personalizado2/weights/best.pt')

# Detección en una imagen
results = model.predict(source='C:/Repos/fotosinventario/nuncaavistoelmodelo/A.jpg', show=True)