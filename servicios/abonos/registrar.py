from archivos.leer import load_database
from archivos.escribir import guardar_database


def agregar_abono(abono_input):
    """Función para agregar un nuevo abono a la base de datos."""
    database = load_database()
    abonos = database.setdefault("abonos", {})
    abono_id = str(len(abonos) + 1)
    abonos[abono_id] = abono_input.model_dump()
    guardar_database(database)
    return {"message": "Abono agregado exitosamente", "abono_id": abono_id}
