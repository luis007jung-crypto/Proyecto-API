from archivos.leer import load_database

def obtener_cliente(cliente_id: str):
    """Endpoint para obtener un cliente por su ID"""
    database = load_database()
    cliente = database.get(cliente_id)
    if cliente:
        return cliente
    else:
        return {"message": "Cliente no encontrado"}, 404
        