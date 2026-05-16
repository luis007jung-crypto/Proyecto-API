from archivos.leer import load_database
from archivos.escribir import guardar_database

def eliminar_producto(producto_id: str):
    """Función para eliminar un producto por su ID"""
    database = load_database()
    if producto_id in database:
        del database[producto_id]
        guardar_database(database)
        return {"message": "Producto eliminado exitosamente"}
    else:
        return {"message": "Producto no encontrado"}, 404