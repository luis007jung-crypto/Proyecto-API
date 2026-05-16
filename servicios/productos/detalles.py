from entidades.ventas import producto_venta
from archivos.leer import load_database
from archivos.escribir import guardar_database

def obtener_producto(producto_id: str):
    """Función para obtener un producto por su ID"""
    database = load_database()
    producto = database.get("productos", {}).get(producto_id)
    if producto:
        return producto
    else:
        return {"message": "Producto no encontrado"}, 404