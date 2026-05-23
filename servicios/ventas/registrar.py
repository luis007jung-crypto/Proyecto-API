from archivos.leer import load_database
from archivos.escribir import guardar_database
from entidades.ventas import Venta


def agregar_venta(venta: Venta):
    """Endpoint para agregar una nueva venta a la base de datos."""
    database = load_database()
    ventas = database.setdefault("ventas", {})

    legacy_venta_ids = [
        int(key)
        for key, value in database.items()
        if str(key).isdigit()
        and isinstance(value, dict)
        and "idventa" in value
        and "idcliente" in value
        and "idproducto" in value
        and "cantidad" in value
        and "fecha" in value
    ]
    section_venta_ids = [int(key) for key in ventas if str(key).isdigit()]

    venta_id = str(max([*legacy_venta_ids, *section_venta_ids], default=0) + 1)
    ventas[venta_id] = venta.model_dump()
    guardar_database(database)
    return {"message": "Venta agregada exitosamente", "venta_id": venta_id}