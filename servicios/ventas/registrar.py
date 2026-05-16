from archivos.leer import load_database
from archivos.escribir import guardar_database
from entidades.ventas import Venta
def agregar_venta(venta: Venta):
    """Endpoint para agregar una nueva venta a la base de datos"""
    database = load_database()
    venta_id = str(len(database) + 1)  # Genera un ID simple basado en el número de ventas
    database[venta_id] = venta
    guardar_database(database)
    return {"message": "Venta agregada exitosamente", "venta_id": venta_id}