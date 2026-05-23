from archivos.leer import load_database
from archivos.escribir import guardar_database


def eliminar_abono(abono_id: str):
    """Función para eliminar un abono por su ID."""
    database = load_database()
    abonos = database.get("abonos", {})
    if abono_id in abonos:
        del abonos[abono_id]
        database["abonos"] = abonos
        guardar_database(database)
        return {"message": "Abono eliminado exitosamente"}
    return {"message": "Abono no encontrado"}, 404