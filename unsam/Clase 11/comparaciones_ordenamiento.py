
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    
    comparaciones = 0
    
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        comparaciones += n
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
        
    return comparaciones
    
def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


#%%

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comparaciones = 0
    for i in range(len(lista) - 1):
        comparaciones += 1
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            pasos = reubicar(lista, i + 1)
            comparaciones += pasos
            
        #print("DEBUG: ", lista)

    return comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    comparaciones = 0
    while j > 0 and v < lista[j - 1]:
        comparaciones += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        
    lista[j] = v
    
    return comparaciones
    
    

#%%
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
            
# lista_1 = [1, 2, -3, 8, 1, 5]
# lista_2 = [1, 2, 3, 4, 5]
# lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
# lista_4 = [10, 8, 6, 2, -2, -5]
# lista_5 = [2, 5, 1, 0]

''' 
El algoritmo es de complejidad cuadratica O(N^2) en el mejor o peor de los casos
puesto que independientemente de si la lista esta ordenada o no, se realiza
siempre el mismo nro de comparaciones ya que cada vuelta solo asegura que el
ultimo elemento analizado se encuentra ordenado

'''
#%%


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comparaciones = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva, comp = merge(izq, der)
        comparaciones += comp
    return lista_nueva, comparaciones

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comparaciones = 0
    while(i < len(lista1[0]) and j < len(lista2[0])):
        comparaciones +=1
        if (lista1[0][i] < lista2[0][j]):
            resultado.append(lista1[0][i])
            i += 1
        else:
            resultado.append(lista2[0][j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[0][i:]
    resultado += lista2[0][j:]

    return resultado, comparaciones




#%%

import random
import numpy as np


def generar_lista(N):

    return [random.randint(1,1000) for _ in range(N)]

def experimento():
    ord_sel = []
    ord_ins = []
    ord_bur = []
    ord_mer = []
    for i in range(1, 257):
        lista = generar_lista(N=i)
        met1 = ord_seleccion(lista.copy())
        met2 = ord_insercion(lista.copy())
        met3 = ord_burbujeo(lista.copy())
        met4 = merge_sort(lista.copy())[1]
        
        ord_sel.append(met1)
        ord_ins.append(met2)
        ord_bur.append(met3)
        ord_mer.append(met4)
            
    return ord_sel, ord_ins, ord_bur, ord_mer

import matplotlib.pyplot as plt

seleccion, insercion, burbujeo, merge = experimento()
x = np.linspace(1, 256, 256, endpoint=True)

# Titulo
plt.title('Complejidad de Ordenamiento')

#Suavizado


# Lineas
#plt.plot(x_new, seleccion_suav)
plt.plot(x, seleccion, color='red', linestyle='dashdot')
plt.plot(x, insercion, color='blue',)
plt.plot(x, burbujeo, color='green', linestyle=':')
plt.plot(x, merge, color='orange')

# Ejes
plt.xlabel('Longitud de la lista')
plt.ylabel('Numero de comparaciones')

# Leyenda
plt.legend(['Seleccion', 'Insercion', 'Burbujeo', 'Merge Sort'])


plt.show()

    
    
    
    
    
    
