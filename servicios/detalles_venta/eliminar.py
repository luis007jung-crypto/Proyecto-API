from archivos.leer import load_database
from archivos.escribir import guardar_database

def eliminar_detalle_venta(id_detalle_venta):
    detalles_venta = load_database('detalles_venta.json')
    for i, detalle in enumerate(detalles_venta):
        if detalle['id'] == id_detalle_venta:
            detalles_venta.pop(i)
            guardar_database('detalles_venta.json', detalles_venta)
            return True
    return False