from archivos.leer import load_database
from archivos.escribir import guardar_database

def eliminar_abono(abono_id: str):
    """Función para eliminar un abono por su ID"""
    database = load_database()
    if abono_id in database:
        del database[abono_id]
        guardar_database(database)
        return {"message": "Abono eliminado exitosamente"}
    else:
        return {"message": "Abono no encontrado"}, 404