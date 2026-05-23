from fastapi import APIRouter

from entidades.ventas import abono
from servicios.abonos.eliminar import eliminar_abono as eliminar_abono_service
from servicios.abonos.listar import listar_abonos as listar_abonos_service
from servicios.abonos.modificar import modificar_abono as modificar_abono_service
from servicios.abonos.registrar import agregar_abono as agregar_abono_service

abonos_router = APIRouter()


@abonos_router.get("/abonos")
def listar_abonos_endpoint():
    """Endpoint para listar todos los abonos."""
    return listar_abonos_service()


@abonos_router.post("/abonos")
def agregar_abono_endpoint(abono_input: abono):
    """Endpoint para agregar un nuevo abono a la base de datos."""
    return agregar_abono_service(abono_input)


@abonos_router.put("/abonos/{abono_id}")
def modificar_abono_endpoint(abono_id: str, abono_input: abono):
    """Endpoint para modificar un abono existente."""
    return modificar_abono_service(abono_id, abono_input)


@abonos_router.delete("/abonos/{abono_id}")
def eliminar_abono_endpoint(abono_id: str):
    """Endpoint para eliminar un abono por su ID."""
    return eliminar_abono_service(abono_id)

