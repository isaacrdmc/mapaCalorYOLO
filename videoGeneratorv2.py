import cv2
import numpy as np

# Configuración del video
frame_width, frame_height = 640, 480
fps = 30
output_filename = "circles_movement.avi"

# Inicializa el video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

# Configuración de los círculos
num_circles = 10
radius = 20
colors = [(0, 0, 255), (0, 255, 0)]  # Rojo y verde en BGR
speed = 5

# Posiciones iniciales y direcciones
circles = [
    {
        "pos": np.array([np.random.randint(radius, frame_width-radius), np.random.randint(radius, frame_height-radius)]),
        "direction": np.random.choice([-1, 1], size=2) * speed,
        "color": colors[i % 2]
    }
    for i in range(num_circles)
]

# Duración del video en segundos
video_duration = 10
num_frames = fps * video_duration

for frame_idx in range(num_frames):
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    
    for circle in circles:
        # Actualizar posición
        circle["pos"] += circle["direction"]
        
        # Detectar colisiones con los bordes y cambiar dirección
        for i in range(2):
            if circle["pos"][i] < radius or circle["pos"][i] > (frame_width if i == 0 else frame_height) - radius:
                circle["direction"][i] *= -1
        
        # Dibujar el círculo
        cv2.circle(frame, tuple(circle["pos"]), radius, circle["color"], -1)
    
    # Escribir el frame al video
    out.write(frame)
    
    # Mostrar el video en tiempo real (opcional)
    # cv2.imshow('Circles Movement', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Liberar recursos
out.release()
cv2.destroyAllWindows()

print(f"Video generado: {output_filename}")
