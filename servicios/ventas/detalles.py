from archivos.leer import load_database


def obtener_ventas(venta_id: str):
    """Endpoint para obtener una venta por su ID."""
    database = load_database()
    ventas = database.get("ventas", {})
    if venta_id in ventas:
        return ventas[venta_id]

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
        return legacy_ventas[venta_id]

    return {"message": "Venta no encontrada"}, 404