from archivos.leer import load_database
from archivos.escribir import guardar_database


def modificar_producto_venta(id_producto_venta, nuevo_producto_venta):
    database = load_database()
    productos_venta = database.get("productos_venta", [])
    for i, pv in enumerate(productos_venta):
        if pv.get("iddetalle") == id_producto_venta:
            productos_venta[i] = nuevo_producto_venta.model_dump()
            database["productos_venta"] = productos_venta
            guardar_database(database)
            return {"message": "Producto de venta actualizado exitosamente"}
    return {"message": "Producto de venta no encontrado"}, 404
    