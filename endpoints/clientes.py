from servicios.clientes.crear import crear_cliente
from servicios.clientes.listar import listar_clientes
from servicios.clientes.obtener import obtener_cliente
from servicios.clientes.actualizar import actualizar_cliente
from servicios.clientes.eliminar import eliminar_cliente
from entidades.clientes import Cliente
from fastapi import APIRouter

clientes_router = APIRouter()

@clientes_router.get("/clientes")
def listar_clients()->list[Cliente]:
    """Endpoint para listar todos los clientes"""
    return listar_clientes()
    
@clientes_router.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: str):
    """Endpoint para obtener un cliente por su ID"""
    return obtener_cliente(cliente_id)


@clientes_router.post("/clientes")
def agregar_cliente(cliente: Cliente):
    """Endpoint para agregar un nuevo cliente a la base de datos"""
    return crear_cliente(cliente)

@clientes_router.put("/clientes/{cliente_id}")
def actualizar_cliente(cliente_id: str, cliente: Cliente):
    """Endpoint para actualizar un cliente existente"""
    return actualizar_cliente(cliente_id, cliente)
    
@clientes_router.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: str):
    """Endpoint para eliminar un cliente por su ID"""
    return eliminar_cliente(cliente_id)