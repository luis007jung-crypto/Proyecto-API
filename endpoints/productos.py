from servicios.productos.agregar import agregar_producto
from servicios.productos.listar import listar_ventas 
from servicios.productos.detalles import obtener_producto
from servicios.productos.editar import editar_producto
from servicios.productos.eliminar import eliminar_producto

from entidades.producto import Producto
from fastapi import APIRouter

productos_router = APIRouter()

@productos_router.get("/productos")
def listar_productos()->list[Producto]:
    """Endpoint para listar todos los productos"""
    return listar_ventas()

@productos_router.get("/productos/{producto_id}")
def obtener_producto(producto_id: str):
    """Endpoint para obtener un producto por su ID"""
    return obtener_producto(producto_id)    

@productos_router.post("/productos")
def agregar_producto(producto: Producto):
    """Endpoint para agregar un nuevo producto a la base de datos"""
    return agregar_producto(producto)

@productos_router.put("/productos/{producto_id}")
def actualizar_producto(producto_id: str, producto: Producto):
    """Endpoint para actualizar un producto existente"""
    return editar_producto(producto_id, producto)   

@productos_router.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: str):    
    """Endpoint para eliminar un producto por su ID"""
    return eliminar_producto(producto_id)