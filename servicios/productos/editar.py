from archivos.leer import load_database
from archivos.escribir import guardar_database

def editar_producto(producto_id: str, nombre: str = None, precio: float = None):
    """Función para editar un producto en la base de datos"""
    database = load_database()
    if producto_id in database:
        producto = database[producto_id]
        if nombre is not None:
            producto["nombre"] = nombre
        if precio is not None:
            producto["precio"] = precio
        database[producto_id] = producto
        guardar_database(database)
        return {"message": "Producto actualizado exitosamente"}
    else:
        return {"message": "Producto no encontrado"}, 404