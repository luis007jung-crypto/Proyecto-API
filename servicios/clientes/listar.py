from archivos.leer import load_database


def listar_clientes():
    database = load_database()
    clientes = database.get("clientes", {})
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
    return list(clientes.values()) + list(legacy_clientes.values())