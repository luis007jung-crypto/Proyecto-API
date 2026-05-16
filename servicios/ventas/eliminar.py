from archivos.leer import load_database
from archivos.escribir import guardar_database
def eliminar_venta(venta_id: str):
    """Endpoint para eliminar una venta por su ID"""
    database = load_database()
    if venta_id in database:
        del database[venta_id]
        guardar_database(database)
        return {"message": "Venta eliminada exitosamente"}
    else:
        return {"message": "Venta no encontrada"}, 404