from ultralytics import YOLO

# Cargar el modelo YOLOv8 preentrenado
model = YOLO('yolov8n.pt')  # Cambiar por 'yolov8s.pt', etc., si quieres usar otro tamaño del modelo.

# Procesar el video
results = model.predict(source="objetos_en_movimiento.mp4", save=True, save_txt=True)
print("Detección completada. Revisa los resultados.")

