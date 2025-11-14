from db_manager import insertar_evento

# prueba simulada
insertar_evento(
    moto_id=1,
    tipo_evento="sin_casco",
    imagen_path="data/images_events/prueba.jpg",
    confianza=0.88
)
