from archivos.leer import load_database
from archivos.escribir import guardar_database


def eliminar_cliente(cliente_id: str):
    """Endpoint para eliminar un cliente por su ID."""
    database = load_database()
    clientes = database.get("clientes", {})

    if cliente_id in clientes:
        del clientes[cliente_id]
        guardar_database(database)
        return {"message": "Cliente eliminado exitosamente"}

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
        del database[cliente_id]
        guardar_database(database)
        return {"message": "Cliente eliminado exitosamente"}

    return {"message": "Cliente no encontrado"}, 404