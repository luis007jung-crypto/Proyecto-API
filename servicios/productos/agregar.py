from archivos.leer import load_database
from archivos.escribir import guardar_database
from entidades.producto import Producto


def agregar_producto(producto: Producto):
    """Endpoint para agregar un nuevo producto."""
    database = load_database()
    productos = database.setdefault("productos", {})
    producto_id = str(producto.idproducto or len(productos) + 1)
    productos[producto_id] = producto.model_dump()
    guardar_database(database)
    return {"message": "Producto agregado exitosamente", "producto_id": producto_id}