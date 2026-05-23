from archivos.leer import load_database
from archivos.escribir import guardar_database
from entidades.producto import Producto


def editar_producto(producto_id: str, producto: Producto):
    """Función para editar un producto en la base de datos."""
    database = load_database()
    productos = database.get("productos", {})
    if producto_id in productos:
        productos[producto_id] = producto.model_dump()
        database["productos"] = productos
        guardar_database(database)
        return {"message": "Producto actualizado exitosamente"}
    return {"message": "Producto no encontrado"}, 404