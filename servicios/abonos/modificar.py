from archivos.leer import load_database
from archivos.escribir import guardar_database

def modificar_abono(abono_id, abono):
    """Función para modificar un abono existente en la base de datos"""
    database = load_database()
    if "abonos" in database and abono_id in database["abonos"]:
        database["abonos"][abono_id] = abono
        guardar_database(database)
        return {"message": "Abono modificado exitosamente"}
    else:
        return {"message": "Abono no encontrado"}, 404