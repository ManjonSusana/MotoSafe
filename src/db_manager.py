import sqlite3
import os
from datetime import datetime

# Carpeta base del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ruta a la base de datos
DB_PATH = os.path.join(BASE_DIR, "db", "motosafe.db")

def insertar_evento(moto_id, tipo_evento, imagen_path, confianza):
    """
    Inserta un evento en la base de datos SQLite.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    creado = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO eventos (fecha, hora, moto_id, tipo_evento, imagen_path, confianza, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (fecha, hora, moto_id, tipo_evento, imagen_path, confianza, creado))

    conn.commit()
    conn.close()

    print(f"[DB] Evento registrado: Moto {moto_id} | {tipo_evento} | {imagen_path}")
