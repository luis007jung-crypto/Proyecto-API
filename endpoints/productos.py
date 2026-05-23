from fastapi import APIRouter

from entidades.producto import Producto
from servicios.productos.agregar import agregar_producto as agregar_producto_service
from servicios.productos.detalles import obtener_producto as obtener_producto_service
from servicios.productos.editar import editar_producto as editar_producto_service
from servicios.productos.eliminar import eliminar_producto as eliminar_producto_service
from servicios.productos.listar import listar_productos as listar_productos_service

productos_router = APIRouter()


@productos_router.get("/productos")
def listar_productos_endpoint():
    """Endpoint para listar todos los productos."""
    return listar_productos_service()


@productos_router.get("/productos/{producto_id}")
def obtener_producto_endpoint(producto_id: str):
    """Endpoint para obtener un producto por su ID."""
    return obtener_producto_service(producto_id)


@productos_router.post("/productos")
def agregar_producto_endpoint(producto: Producto):
    """Endpoint para agregar un nuevo producto a la base de datos."""
    return agregar_producto_service(producto)


@productos_router.put("/productos/{producto_id}")
def actualizar_producto_endpoint(producto_id: str, producto: Producto):
    """Endpoint para actualizar un producto existente."""
    return editar_producto_service(producto_id, producto)


@productos_router.delete("/productos/{producto_id}")
def eliminar_producto_endpoint(producto_id: str):
    """Endpoint para eliminar un producto por su ID."""
    return eliminar_producto_service(producto_id)