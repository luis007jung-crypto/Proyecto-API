from archivos.leer import load_database


def obtener_cliente(cliente_id: str):
    """Endpoint para obtener un cliente por su ID."""
    database = load_database()
    clientes = database.get("clientes", {})
    if cliente_id in clientes:
        return clientes[cliente_id]

    legacy_clientes = {
        key: value
        for key, value in database.items()
        if str(key).isdigit()
        and isinstance(value, dict)
        and "idventa" not in value
        and "idproducto" not in value
        and "cantidad" not in value
        and "fecha" not in value
    }
    if cliente_id in legacy_clientes:
        return legacy_clientes[cliente_id]

    return {"message": "Cliente no encontrado"}, 404