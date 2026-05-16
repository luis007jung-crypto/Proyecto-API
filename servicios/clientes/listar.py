from entidades.clientes import Cliente
from archivos.leer import load_database

def listar_clientes()->list[Cliente]:
 database = load_database()
 return database