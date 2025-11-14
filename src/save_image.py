import cv2
import os
from datetime import datetime

# Carpeta base del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Carpeta donde se guardarán las capturas
IMAGES_DIR = os.path.join(BASE_DIR, "data", "images_events")
os.makedirs(IMAGES_DIR, exist_ok=True)

def guardar_imagen(frame, moto_id):
    """
    Guarda el frame actual como captura cuando se detecta una moto sin casco.
    Retorna la ruta completa de la imagen guardada.
    """
    fecha = datetime.now().strftime("%Y%m%d")
    hora = datetime.now().strftime("%H%M%S")

    filename = f"moto_{moto_id}_{fecha}_{hora}.jpg"
    file_path = os.path.join(IMAGES_DIR, filename)

    cv2.imwrite(file_path, frame)

    print(f"[IMG] Captura guardada: {file_path}")

    return file_path
