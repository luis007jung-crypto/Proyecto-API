from servicios.abonos.registrar import agregar_abono    
from servicios.abonos.listar import listar_abonos
from servicios.abonos.modificar import modificar_abono
from servicios.abonos.eliminar import eliminar_abono
from entidades.ventas import abono
from fastapi import APIRouter

abonos_router = APIRouter()

@abonos_router.get("/abonos")
def listar_abonos_endpoint()->list[abono]:
    """Endpoint para listar todos los abonos"""
    return listar_abonos()

@abonos_router.post("/abonos")
def agregar_abono_endpoint(abono: abono):    
    """Endpoint para agregar un nuevo abono a la base de datos"""
    return agregar_abono(abono)

@abonos_router.put("/abonos/{abono_id}")
def modificar_abono_endpoint(abono_id: str, abono: abono):
    """Endpoint para modificar un abono existente"""
    return modificar_abono(abono_id, abono)

@abonos_router.delete("/abonos/{abono_id}")
def eliminar_abono_endpoint(abono_id: str):   
    """Endpoint para eliminar un abono por su ID"""
    return eliminar_abono(abono_id)

