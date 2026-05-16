from pydantic import BaseModel

class Venta(BaseModel):
    idventa: str
    idcliente: str
    idproducto: str
    cantidad: int
    fecha: str

class producto_venta(BaseModel):
    iddetalle: str
    idventa: str
    idproducto: str
    cantidad: int
    precio : float
    subtotal : float

class abono(BaseModel):
    idabono: str
    idventa: str
    monto: float
    fecha: str
