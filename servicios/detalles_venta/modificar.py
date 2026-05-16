from archivos.leer import load_database 
from archivos.escribir import guardar_database

def modificar_detalle_venta(id_detalle_venta, detalle_venta_modificado):
    detalles_venta = load_database('detalles_venta.json')
    for i, detalle in enumerate(detalles_venta):
        if detalle['id'] == id_detalle_venta:
            detalles_venta[i] = detalle_venta_modificado
            guardar_database('detalles_venta.json', detalles_venta)
            return detalle_venta_modificado
    return None