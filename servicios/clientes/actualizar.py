from archivos.leer import load_database
from archivos.escribir import guardar_database
from entidades.clientes import Cliente

def actualizar_cliente(cliente_id: str, cliente: Cliente):
 """Endpoint para actualizar un cliente existente"""
 database = load_database()
 if cliente_id in database:
        database[cliente_id] = cliente
        guardar_database(database)
        return {"message": "Cliente actualizado exitosamente"}
 else:
        return {"message": "Cliente no encontrado"}, 404
