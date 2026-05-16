from archivos.leer import load_database
from archivos.escribir import guardar_database

def agregar_producto(producto_id: str, producto: dict):
    """Endpoint para agregar un nuevo producto"""
    database = load_database()
    if "productos" not in database:
        database["productos"] = {}
    database["productos"][producto_id] = producto
    guardar_database(database)
    return {"message": "Producto agregado exitosamente", "producto_id": producto_id}