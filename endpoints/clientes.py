from fastapi import APIRouter

from entidades.clientes import Cliente
from servicios.clientes.actualizar import actualizar_cliente as actualizar_cliente_service
from servicios.clientes.crear import crear_cliente as crear_cliente_service
from servicios.clientes.eliminar import eliminar_cliente as eliminar_cliente_service
from servicios.clientes.listar import listar_clientes as listar_clientes_service
from servicios.clientes.obtener import obtener_cliente as obtener_cliente_service

clientes_router = APIRouter()


@clientes_router.get("/clientes")
def listar_clients():
    """Endpoint para listar todos los clientes."""
    return listar_clientes_service()


@clientes_router.get("/clientes/{cliente_id}")
def obtener_cliente_endpoint(cliente_id: str):
    """Endpoint para obtener un cliente por su ID."""
    return obtener_cliente_service(cliente_id)


@clientes_router.post("/clientes")
def agregar_cliente_endpoint(cliente: Cliente):
    """Endpoint para agregar un nuevo cliente a la base de datos."""
    return crear_cliente_service(cliente)


@clientes_router.put("/clientes/{cliente_id}")
def actualizar_cliente_endpoint(cliente_id: str, cliente: Cliente):
    """Endpoint para actualizar un cliente existente."""
    return actualizar_cliente_service(cliente_id, cliente)


@clientes_router.delete("/clientes/{cliente_id}")
def eliminar_cliente_endpoint(cliente_id: str):
    """Endpoint para eliminar un cliente por su ID."""
    return eliminar_cliente_service(cliente_id)