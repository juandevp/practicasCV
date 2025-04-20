# 📊 Reporte de Resultados del Modelo YOLOv8 – Detección de Botellas y Cajas

## ✅ Resumen General

El modelo fue entrenado para detectar dos clases: **botella** y **caja**. Se utilizaron herramientas de análisis visual como histogramas, matrices de confusión, curvas métricas y pérdidas para validar el rendimiento del modelo.

---

## 📦 Distribución de Etiquetas

- **Cantidad de Instancias:**
  - Caja: 350+
  - Botella: 230+
- **Observación:**  
  El dataset presenta un leve desbalance a favor de la clase “caja”. Esto podría influir en la capacidad del modelo para detectar botellas con la misma precisión.

- **Distribución Espacial:**  
  Las anotaciones están bien distribuidas en el eje `x` e `y`, lo cual es deseable. La mayoría de los objetos tienen tamaños consistentes (width y height), aunque algunas instancias son significativamente más grandes.

---

## 📉 Comportamiento Durante el Entrenamiento

- **Pérdidas de entrenamiento y validación (`results.png`):**
  - Las pérdidas (`box_loss`, `cls_loss`, `dfl_loss`) descienden consistentemente.
  - No hay evidencia de overfitting, ya que las curvas de validación también mejoran.

- **Métricas alcanzadas:**
  - mAP@0.5 ≈ **0.93**
  - mAP@0.5:0.95 ≈ **0.85**
  - Precisión y recall por encima de 0.90 para ambas clases.

✔️ **Diagnóstico:**  
El modelo muestra un **muy buen desempeño general**. Las métricas son adecuadas para pasar a producción o pruebas en campo controlado.

---

## 🔍 Matrices de Confusión

- **Confusion Matrix (valores absolutos):**
  - Caja: 102 predicciones correctas, 14 confusiones con botellas.
  - Botella: 53 aciertos, 16 confundidas con cajas.

- **Matriz Normalizada:**
  - Caja: precisión de 99%, recall de 47%.
  - Botella: precisión de 100%, recall de 53%.

❗ **Conclusión:**  
El modelo **confunde cajas con botellas más que viceversa**. Aunque la precisión es alta, el **recall bajo sugiere que hay objetos no detectados**. 

---

## 📈 Curvas de Métricas vs Confianza

### Precision-Recall Curve
- Caja: **0.935**
- Botella: **0.924**
- mAP@0.5 general: **0.929**

### F1-Confidence Curve
- Mejor umbral de confianza ≈ **0.30**
- F1-score óptimo: **0.90**

📌 **Recomendación:**  
Ajustar el **umbral de confianza a 0.30** para maximizar el balance entre precisión y recall.

---

## ✅ ¿El Modelo Está Bien?

**Sí, el modelo está bien entrenado**, con métricas destacables. Sin embargo, hay **áreas de mejora**:

### 🔧 Ajustes Recomendados

1. **Balancear las clases:**  
   Aumentar imágenes de la clase "botella" o aplicar técnicas de augmentación específicas.
   
2. **Ajustar el umbral de confianza (conf):**  
   Establecer `conf=0.30` para obtener mejor F1 y recall.

3. **Reentrenar con `imgsz` mayor si es posible:**  
   Mejora la precisión en objetos pequeños si tu hardware lo permite.

4. **Validar en campo real:**  
   Asegurar que el rendimiento en producción sea coherente con los resultados de validación.
