from archivos.leer import load_database
from archivos.escribir import guardar_database
from entidades.ventas import Venta
def actualizar_venta(venta_id: str, venta: Venta):
    """Endpoint para actualizar una venta existente"""
    database = load_database()
    if venta_id in database:
        database[venta_id] = venta
        guardar_database(database)
        return {"message": "Venta actualizada exitosamente"}
    else:
        return {"message": "Venta no encontrada"}, 404