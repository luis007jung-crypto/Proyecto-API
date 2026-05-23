import json
from pathlib import Path

DATABASE_FILE = Path(__file__).resolve().parent.parent / "database.json"


def guardar_database(database):
    """Función para guardar la base de datos en un archivo JSON."""
    with DATABASE_FILE.open("w", encoding="utf-8") as archivo:
        json.dump(database, archivo, indent=4, ensure_ascii=False)