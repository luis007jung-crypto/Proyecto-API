from archivos.leer import load_database
from archivos.escribir import guardar_database

def modificar_producto_venta(id_producto_venta, nuevo_producto_venta):
    database = load_database()
    productos_venta = database.get("productos_venta", [])
    for i, pv in enumerate(productos_venta):
        if pv["id"] == id_producto_venta:
            productos_venta[i] = nuevo_producto_venta
            break
    database["productos_venta"] = productos_venta
    guardar_database(database)
    