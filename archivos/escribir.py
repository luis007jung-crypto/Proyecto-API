from main import JSON_DATABASE_FILE
import json

def guardar_database(database):
    """Función para guardar la base de datos en un archivo JSON"""
    with open(JSON_DATABASE_FILE, "w") as f:
        json.dump(database, f, indent=4)