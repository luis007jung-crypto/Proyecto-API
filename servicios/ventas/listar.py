from archivos.leer import load_database


def listar_ventas():
    """Endpoint para listar las ventas."""
    database = load_database()
    ventas = database.get("ventas", {})
    legacy_ventas = {
        key: value
        for key, value in database.items()
        if str(key).isdigit()
        and isinstance(value, dict)
        and "idventa" in value
        and "idcliente" in value
        and "idproducto" in value
        and "cantidad" in value
        and "fecha" in value
    }
    return list(ventas.values()) + list(legacy_ventas.values())