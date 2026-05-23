import json
from pathlib import Path

DATABASE_FILE = Path(__file__).resolve().parent.parent / "database.json"


def load_database():
    """Función para cargar la base de datos desde un archivo JSON."""
    try:
        with DATABASE_FILE.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}