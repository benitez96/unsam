
def ord_burbujeo(lista, debug=False):
    
    n = len(lista)-1
    
    if debug:
        print('{:^10s} - {:^20s}'.format('N', 'LISTA'))    
    comparaciones = 0
    while n:
        
        if debug:
            print(f'{n:^10} -   {lista}')
            
        for i in range(n):
            comparaciones += 1
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
            
        n -= 1
        
    return comparaciones
            
lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]

''' 
El algoritmo es de complejidad cuadratica O(N^2) en el mejor o peor de los casos
puesto que independientemente de si la lista esta ordenada o no, se realiza
siempre el mismo nro de comparaciones ya que cada vuelta solo asegura que el
ultimo elemento analizado se encuentra ordenado

'''
