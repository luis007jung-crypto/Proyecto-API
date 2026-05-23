from archivos.leer import load_database
from archivos.escribir import guardar_database


def eliminar_venta(venta_id: str):
    """Endpoint para eliminar una venta por su ID."""
    database = load_database()
    ventas = database.get("ventas", {})

    if venta_id in ventas:
        del ventas[venta_id]
        guardar_database(database)
        return {"message": "Venta eliminada exitosamente"}

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
        del database[venta_id]
        guardar_database(database)
        return {"message": "Venta eliminada exitosamente"}

    return {"message": "Venta no encontrada"}, 404