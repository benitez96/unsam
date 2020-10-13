# ticker.py

from vigilante import vigilar
import csv
import informe
from formato_tabla import crear_formateador, imprimir_tabla

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(filas, nombres):
    rows = (fila for fila in filas if fila['nombre'] in nombres)
    return rows
    
    """ for fila in filas:
        if fila['nombre'] in nombres:       #version anterior
            yield fila
 """

def ticker(camion_file, log_file, fmt):

    formateador = crear_formateador(fmt)
    camion = informe.leer_camion('Data/camion.csv')
    formateador.encabezado(['nombre', 'precio', 'volumen']) #seteo headers
    filas = parsear_datos(vigilar('Data/mercadolog.csv'))
    filas = filtrar_datos(filas, camion)
    for fila in filas:
        formateador.fila(str(v) for v in fila.values())              #seteo filas


if __name__ == '__main__':
    
    ticker('Data/camion.csv', 'Data/mercadolog.csv', 'csv')