from archivos.leer import load_database
from archivos.escribir import guardar_database


def eliminar_producto_venta(id_producto_venta):
    database = load_database()
    productos_venta = database.get("productos_venta", [])
    filtered = [pv for pv in productos_venta if pv.get("iddetalle") != id_producto_venta]
    if len(filtered) == len(productos_venta):
        return {"message": "Producto de venta no encontrado"}, 404
    database["productos_venta"] = filtered
    guardar_database(database)
    return {"message": "Producto de venta eliminado exitosamente"}
    