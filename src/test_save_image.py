import numpy as np
import cv2
from save_image import guardar_imagen

# crear imagen de prueba (un cuadrado negro)
frame = np.zeros((480, 640, 3), dtype=np.uint8)
cv2.putText(frame, "MotoSafe Test", (100, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

# probar guardado
ruta = guardar_imagen(frame, moto_id=99)
print("Imagen guardada en:", ruta)
