def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0, e)
    return invertida

lista = [
    'Bogotá',
    'Rosario',
    'Santiago',
    'San Fernando',
    'San Miguel'
    ]
print(invertir_lista(lista))