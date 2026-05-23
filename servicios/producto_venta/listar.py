from archivos.leer import load_database
from archivos.escribir import guardar_database

def listar_productos_venta():
    database = load_database()
    productos_venta = database.get("productos_venta", [])
    return productos_venta  
