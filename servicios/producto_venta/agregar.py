from archivos.leer import load_database
from archivos.escribir import guardar_database

def agregar_producto_venta(producto_venta):
    database = load_database()
    productos_venta = database.get("productos_venta", [])
    productos_venta.append(producto_venta)
    database["productos_venta"] = productos_venta
    guardar_database(database)
    