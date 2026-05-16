from main import JSON_DATABASE_FILE
import json

def load_database():
    """Función para cargar la base de datos desde un archivo JSON"""
    try:
        with open(JSON_DATABASE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Retorna una base de datos vacía si no existe el archivo