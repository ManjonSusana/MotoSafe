import cv2
import numpy as np
from ultralytics import YOLO
import os

# Cargar YOLOv8
model = YOLO("yolov8n.pt")

def es_casco(region_cabeza):
    gray = cv2.cvtColor(region_cabeza, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7,7), 0)

    # Detección de círculos
    circles = cv2.HoughCircles(
        gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
        param1=50, param2=28, minRadius=10, maxRadius=60
    )
    if circles is not None:
        return True

    # Detección de brillo
    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    brillo = cv2.countNonZero(thresh)
    return brillo > 200

def procesar_video(ruta_video):
    print("Intentando abrir:", ruta_video)
    cap = cv2.VideoCapture(ruta_video)

    if not cap.isOpened():
        print("❌ No se pudo abrir el video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.4)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                x1,y1,x2,y2 = map(int, box.xyxy[0])

                # detectar solo "persona"
                if cls == 0:
                    head_y1 = y1
                    head_y2 = y1 + int((y2-y1)*0.35)
                    head = frame[head_y1:head_y2, x1:x2]

                    if head.size == 0:
                        continue

                    if es_casco(head):
                        texto = "CON CASCO"
                        color = (0,255,0)
                    else:
                        texto = "SIN CASCO"
                        color = (0,0,255)

                    cv2.putText(frame, texto, (x1,y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        cv2.imshow("MotoSafe - Casco/No Casco", frame)
        if cv2.waitKey(1) & 0xFF == 27: # tecla ESC
            break

    cap.release()
    cv2.destroyAllWindows()

# RUTA ABSOLUTA DEL VIDEO
ruta_video = r"S:\MotoSafe\data\videos_raw\video2.mp4"
procesar_video(ruta_video)
