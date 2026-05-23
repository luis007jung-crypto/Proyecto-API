from archivos.leer import load_database
from archivos.escribir import guardar_database


def crear_cliente(cliente):
    database = load_database()
    clientes = database.setdefault("clientes", {})

    legacy_client_ids = [
        int(key)
        for key, value in database.items()
        if str(key).isdigit()
        and isinstance(value, dict)
        and "idventa" not in value
        and "idproducto" not in value
        and "cantidad" not in value
        and "fecha" not in value
    ]
    section_client_ids = [int(key) for key in clientes if str(key).isdigit()]

    cliente_id = str(max([*legacy_client_ids, *section_client_ids], default=0) + 1)
    clientes[cliente_id] = cliente.model_dump()
    guardar_database(database)
    return {"message": "Cliente agregado exitosamente", "cliente_id": cliente_id}