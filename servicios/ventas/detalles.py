from archivos.leer import load_database
def obtener_ventas(venta_id: str):
    """Endpoint para obtener una venta por su ID"""
    database = load_database()
    venta = database.get(venta_id)
    if venta:
        return venta
    else:
        return {"message": "Venta no encontrada"}, 404
    