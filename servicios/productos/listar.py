from archivos.leer import load_database


def listar_productos():
    """Endpoint para listar los productos."""
    database = load_database()
    return list(database.get("productos", {}).values())
