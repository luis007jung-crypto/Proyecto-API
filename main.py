from fastapi import FastAPI

from endpoints.clientes import clientes_router
from endpoints.productos import productos_router
from endpoints.abonos import abonos_router
from endpoints.ventas import ventas_router
from endpoints.producto_venta import producto_venta_router

app = FastAPI()

app.include_router(clientes_router)
app.include_router(productos_router)
app.include_router(abonos_router)
app.include_router(ventas_router)
app.include_router(producto_venta_router)

"""prueba de commit"""
