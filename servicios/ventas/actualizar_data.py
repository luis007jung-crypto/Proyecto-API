from archivos.leer import load_database
from archivos.escribir import guardar_database
from entidades.ventas import Venta


def actualizar_venta(venta_id: str, venta: Venta):
    """Endpoint para actualizar una venta existente."""
    database = load_database()
    ventas = database.get("ventas", {})

    if venta_id in ventas:
        ventas[venta_id] = venta.model_dump()
        guardar_database(database)
        return {"message": "Venta actualizada exitosamente"}

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
    if venta_id in legacy_ventas:
        database[venta_id] = venta.model_dump()
        guardar_database(database)
        return {"message": "Venta actualizada exitosamente"}

    return {"message": "Venta no encontrada"}, 404