from archivos.leer import load_database

def listar_abonos():
    """Función para listar los abonos"""
    database = load_database()
    return database.get("abonos", {})