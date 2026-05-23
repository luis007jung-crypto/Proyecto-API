from archivos.leer import load_database
from archivos.escribir import guardar_database

def eliminar_producto_venta(id_producto_venta):
    database = load_database()
    productos_venta = database.get("productos_venta", [])
    productos_venta = [pv for pv in productos_venta if pv["id"] != id_producto_venta]
    database["productos_venta"] = productos_venta
    guardar_database(database)
    