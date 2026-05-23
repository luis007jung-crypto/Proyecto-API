from fastapi import APIRouter

from entidades.ventas import producto_venta
from servicios.producto_venta.agregar import agregar_producto_venta as agregar_producto_venta_service
from servicios.producto_venta.eliminar import eliminar_producto_venta as eliminar_producto_venta_service
from servicios.producto_venta.listar import listar_productos_venta as listar_productos_venta_service
from servicios.producto_venta.modificar import modificar_producto_venta as modificar_producto_venta_service

producto_venta_router = APIRouter()


@producto_venta_router.get("/producto_venta")
def listar_productos_venta_endpoint():
    """Endpoint para listar todos los productos de venta."""
    return listar_productos_venta_service()


@producto_venta_router.post("/producto_venta")
def agregar_producto_venta_endpoint(producto: producto_venta):
    """Endpoint para agregar un nuevo producto de venta a la base de datos."""
    return agregar_producto_venta_service(producto)


@producto_venta_router.put("/producto_venta/{producto_id}")
def modificar_producto_venta_endpoint(producto_id: str, producto: producto_venta):
    """Endpoint para modificar un producto de venta existente."""
    return modificar_producto_venta_service(producto_id, producto)


@producto_venta_router.delete("/producto_venta/{producto_id}")
def eliminar_producto_venta_endpoint(producto_id: str):
    """Endpoint para eliminar un producto de venta por su ID."""
    return eliminar_producto_venta_service(producto_id)

