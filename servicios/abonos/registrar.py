from archivos.leer import load_database
from archivos.escribir import guardar_database

def agregar_abono(abono):
    """Función para agregar un nuevo abono a la base de datos"""
    database = load_database()
    abono_id = str(len(database.get("abonos", {})) + 1)  # Genera un ID simple basado en el número de abonos
    if "abonos" not in database:
        database["abonos"] = {}
    database["abonos"][abono_id] = abono
    guardar_database(database)
    return {"message": "Abono agregado exitosamente", "abono_id": abono_id}
