from fastapi import FastAPI
import json
from pydantic import BaseModel

api = FastAPI()

JSON_DATABASE_FILE = "database.json"


def load_database():
    """Función para cargar la base de datos desde un archivo JSON"""
    try:
        with open(JSON_DATABASE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Retorna una base de datos vacía si no existe el archivo

def guardar_database(database):
    """Función para guardar la base de datos en un archivo JSON"""
    with open(JSON_DATABASE_FILE, "w") as f:
        json.dump(database, f, indent=4)

@api.get("/")
def read_root():
    return {"Hello": "World"}

class Cliente(BaseModel):
    idnombre: str
    nombre: str
    telefono: str

@api.get("/clientes")
def listar_clients()->list[Cliente]:
    """Endpoint para listar los clientes"""
    database = load_database()
    return database


@api.post("/clientes")
def agregar_cliente(cliente: Cliente):
    """Endpoint para agregar un nuevo cliente a la base de datos"""
    database = load_database()
    cliente_id = str(len(database) + 1)  # Genera un ID simple basado en el número de clientes
    database[cliente_id] = cliente
    guardar_database(database)
    return {"message": "Cliente agregado exitosamente", "cliente_id": cliente_id}
