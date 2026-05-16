from archivos.leer import load_database


def listar_ventas():
    """Endpoint para listar las ventas"""
    database = load_database()
    return database
