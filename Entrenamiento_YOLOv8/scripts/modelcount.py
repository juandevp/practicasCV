# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 21:36:09 2025

@author: juanc
"""

import cv2
from ultralytics import YOLO
from collections import Counter

# Cargar el modelo entrenado
model = YOLO('C:/Repos/practicasCV/Entrenamiento_YOLOv8/dataset/runs/detect/modelo_personalizado2/weights/best.pt')

# Leer la imagen original
ruta_imagen = "C:/Repos/fotosinventario/nuncaavistoelmodelo/A.jpg"  # Cambia por tu imagen
imagen_original = cv2.imread(ruta_imagen)

# Ejecutar la predicción
resultados = modelo(ruta_imagen)[0]

# Obtener clases detectadas
clases_detectadas = resultados.boxes.cls.cpu().numpy().astype(int)
nombres_clases = modelo.names
conteo = Counter(clases_detectadas)

# Dibujar la imagen con anotaciones (boxes, labels, etc.)
imagen_anotada = resultados.plot()

# Construir el texto con el conteo
texto = "  ".join([f"{nombres_clases[c]}: {conteo[c]}" for c in conteo])

# Agregar fondo negro arriba para el texto
alto_texto = 40
imagen_anotada = cv2.copyMakeBorder(imagen_anotada, alto_texto, 0, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))

# Poner el texto en la parte superior
cv2.putText(imagen_anotada, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Mostrar resultado
cv2.imshow("Detección con Conteo", imagen_anotada)
cv2.waitKey(0)
cv2.destroyAllWindows()
