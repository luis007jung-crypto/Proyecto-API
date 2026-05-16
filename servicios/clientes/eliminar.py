from archivos.leer import load_database
from archivos.escribir import guardar_database


def eliminar_cliente(cliente_id: str):
    """Endpoint para eliminar un cliente por su ID"""
    database = load_database()
    if cliente_id in database:
        del database[cliente_id]
        guardar_database(database)
        return {"message": "Cliente eliminado exitosamente"}
    else:
        return {"message": "Cliente no encontrado"}, 404

