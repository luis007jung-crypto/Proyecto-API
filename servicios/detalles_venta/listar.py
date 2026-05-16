from archivos.leer import load_database

def listar_detalles_venta():
    detalles_venta = load_database('detalles_venta.json')
    return detalles_venta