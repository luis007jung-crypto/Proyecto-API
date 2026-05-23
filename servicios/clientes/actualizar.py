from archivos.leer import load_database
from archivos.escribir import guardar_database
from entidades.clientes import Cliente


def actualizar_cliente(cliente_id: str, cliente: Cliente):
    """Endpoint para actualizar un cliente existente."""
    database = load_database()
    clientes = database.get("clientes", {})

    if cliente_id in clientes:
        clientes[cliente_id] = cliente.model_dump()
        guardar_database(database)
        return {"message": "Cliente actualizado exitosamente"}

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
        database[cliente_id] = cliente.model_dump()
        guardar_database(database)
        return {"message": "Cliente actualizado exitosamente"}

    return {"message": "Cliente no encontrado"}, 404
