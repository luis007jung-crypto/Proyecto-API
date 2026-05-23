from fastapi import APIRouter

from entidades.ventas import Venta
from servicios.ventas.actualizar_data import actualizar_venta as actualizar_venta_service
from servicios.ventas.detalles import obtener_ventas as obtener_ventas_service
from servicios.ventas.eliminar import eliminar_venta as eliminar_venta_service
from servicios.ventas.listar import listar_ventas as listar_ventas_service
from servicios.ventas.registrar import agregar_venta as agregar_venta_service

ventas_router = APIRouter()


@ventas_router.get("/ventas")
def listar_ventas_endpoint():
    """Endpoint para listar todas las ventas."""
    return listar_ventas_service()


@ventas_router.get("/ventas/{venta_id}")
def obtener_venta_endpoint(venta_id: str):
    """Endpoint para obtener una venta por su ID."""
    return obtener_ventas_service(venta_id)


@ventas_router.post("/ventas")
def agregar_venta_endpoint(venta: Venta):
    """Endpoint para agregar una nueva venta a la base de datos."""
    return agregar_venta_service(venta)


@ventas_router.put("/ventas/{venta_id}")
def actualizar_venta_endpoint(venta_id: str, venta: Venta):
    """Endpoint para actualizar una venta existente."""
    return actualizar_venta_service(venta_id, venta)


@ventas_router.delete("/ventas/{venta_id}")
def eliminar_venta_endpoint(venta_id: str):
    """Endpoint para eliminar una venta por su ID."""
    return eliminar_venta_service(venta_id)

