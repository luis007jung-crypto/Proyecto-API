from archivos.leer import load_database
from archivos.escribir import guardar_database


def eliminar_producto(producto_id: str):
    """Función para eliminar un producto por su ID."""
    database = load_database()
    productos = database.get("productos", {})
    if producto_id in productos:
        del productos[producto_id]
        database["productos"] = productos
        guardar_database(database)
        return {"message": "Producto eliminado exitosamente"}
    return {"message": "Producto no encontrado"}, 404