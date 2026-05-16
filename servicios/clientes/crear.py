from archivos.leer import load_database
from archivos.escribir import guardar_database

def crear_cliente(cliente):
    database = load_database()
    cliente_id = str(len(database) + 1)  # Genera un ID simple basado en el número de clientes
    database[cliente_id] = cliente
    guardar_database(database)
    return {"message": "Cliente agregado exitosamente", "cliente_id": cliente_id}