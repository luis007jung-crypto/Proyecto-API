from fastapi import FastAPI

api = FastAPI()

from endpoints.clientes import clientes_router
from endpoints.productos import productos_router
from endpoints.abonos import abonos_router


JSON_DATABASE_FILE = "database.json"
app = FastAPI()

    
app.include_router(clientes_router)
app.include_router(productos_router)
app.include_router(abonos_router)

