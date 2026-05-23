from servicios.ventas.registrar import agregar_venta
from servicios.ventas.listar import listar_ventas
from servicios.ventas.actualizar_data import actualizar_venta
from servicios.ventas.eliminar import eliminar_venta
from servicios.ventas.detalles import obtener_ventas
from entidades.ventas import Venta
from fastapi import APIRouter

ventas_router = APIRouter()

@ventas_router.get("/ventas")
def listar_ventas_endpoint()->list[Venta]:
    """Endpoint para listar todas las ventas"""
    return listar_ventas()

@ventas_router.get("/ventas/{venta_id}")
def obtener_venta(venta_id: str):
    """Endpoint para obtener una venta por su ID"""
    return obtener_ventas(venta_id) 

@ventas_router.post("/ventas")
def agregar_venta_endpoint(venta: Venta):
    """Endpoint para agregar una nueva venta a la base de datos"""
    return agregar_venta(venta)

@ventas_router.put("/ventas/{venta_id}")
def actualizar_venta_endpoint(venta_id: str, venta: Venta):
    """Endpoint para actualizar una venta existente"""
    return actualizar_venta(venta_id, venta)    

@ventas_router.delete("/ventas/{venta_id}")
def eliminar_venta_endpoint(venta_id: str): 
    """Endpoint para eliminar una venta por su ID"""
    return eliminar_venta(venta_id)

