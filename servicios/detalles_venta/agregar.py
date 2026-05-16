from archivos.leer import load_database
from archivos.escribir import guardar_database

def agregar_detalle_venta(detalle_venta):
    detalles_venta = load_database('detalles_venta.json')
    detalles_venta.append(detalle_venta)
    guardar_database('detalles_venta.json', detalles_venta)
    return detalle_venta