
from pydantic import BaseModel


class Cliente(BaseModel):
    idnombre: str
    nombre: str
    telefono: str