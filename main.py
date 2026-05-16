from fastapi import FastAPI
import json
from fastapi import APIRouter
from pydantic import BaseModel
from archivos.leer import load_database
from servicios.clientes.crear import crear_cliente
from servicios.clientes.listar import listar_clientes
from servicios.clientes.obtener import obtener_cliente
from servicios.clientes.actualizar import actualizar_cliente
from servicios.clientes.eliminar import eliminar_cliente
api = FastAPI()
from entidades.clientes import Cliente


JSON_DATABASE_FILE = "database.json"
app = FastAPI()
router = APIRouter()

@router.get("/clientes")
def listar_clients()->list[Cliente]:
    """Endpoint para listar todos los clientes"""
    return listar_clientes()



@api.get("/ventas")
def listar_ventas():
    """Endpoint para listar las ventas"""
    database = load_database()
    return database

@api.get("/ventas/{venta_id}")
def obtener_ventas(venta_id: str):
    """Endpoint para obtener una venta por su ID"""
    database = load_database()
    venta = database.get(venta_id)
    if venta:
        return venta
    else:
        return {"message": "Venta no encontrada"}, 404
    
@api.post("/ventas")
def agregar_venta(venta: Venta):
    """Endpoint para agregar una nueva venta a la base de datos"""
    database = load_database()
    venta_id = str(len(database) + 1)  # Genera un ID simple basado en el número de ventas
    database[venta_id] = venta
    guardar_database(database)
    return {"message": "Venta agregada exitosamente", "venta_id": venta_id}

@api.put("/ventas/{venta_id}")
def actualizar_venta(venta_id: str, venta: Venta):
    """Endpoint para actualizar una venta existente"""
    database = load_database()
    if venta_id in database:
        database[venta_id] = venta
        guardar_database(database)
        return {"message": "Venta actualizada exitosamente"}
    else:
        return {"message": "Venta no encontrada"}, 404
    
@api.delete("/ventas/{venta_id}")
def eliminar_venta(venta_id: str):
    """Endpoint para eliminar una venta por su ID"""
    database = load_database()
    if venta_id in database:
        del database[venta_id]
        guardar_database(database)
        return {"message": "Venta eliminada exitosamente"}
    else:
        return {"message": "Venta no encontrada"}, 404
    