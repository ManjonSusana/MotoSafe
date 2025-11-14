import sqlite3
import os

# Carpeta base del proyecto (un nivel arriba de src)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Carpeta db dentro del proyecto
DB_DIR = os.path.join(BASE_DIR, "db")
os.makedirs(DB_DIR, exist_ok=True)  # asegurarnos que exista

# Ruta completa del archivo de base de datos
DB_PATH = os.path.join(DB_DIR, "motosafe.db")

def create_database():
    print(f"Creando base de datos en: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Crear tabla de eventos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            moto_id INTEGER,
            tipo_evento TEXT,
            imagen_path TEXT,
            confianza REAL,
            created_at TEXT
        );
    """)

    conn.commit()
    conn.close()
    print("Base de datos creada correctamente.")

if __name__ == "__main__":
    create_database()
