from archivos.leer import load_database


def obtener_producto(producto_id: str):
    """Función para obtener un producto por su ID."""
    database = load_database()
    producto = database.get("productos", {}).get(producto_id)
    if producto:
        return producto
    return {"message": "Producto no encontrado"}, 404