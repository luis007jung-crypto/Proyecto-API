
from pydantic import BaseModel

class Producto(BaseModel):
    idproducto: str
    nombre: str
    precio: float