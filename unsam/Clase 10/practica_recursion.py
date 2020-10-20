#%% Ejercicio 10.2: Números triangulares

def suma_triangular(n):
    ''' Precondicion: n>=0
    Devuelve: la sumatoria de cada numero desde 0 hasta n.
    '''
    if n==0:
        return 0
    return n + suma_triangular(n-1)

#%% Ejercicio 10.3: Dígitos

def digitos(n):
    '''Precondicion: n>0
    devuelve: El numero de digitos de n.
    '''
    n = str(n)    
    if len(n) == 0:
        return 0
        
            
    return 1 + digitos(n[1:])
    
    
#%% Ejercicio 10.4: Potencias

def es_potencia(n,b):
    
    '''  precondicion: n y b son enteros positivos.
    devuelve: True si n es potencia de b.
    '''
    
    potencia=False
    
    if n==1:
        potencia=True
        return potencia
    elif n<1:
        return potencia
    else:
        potencia = es_potencia(n/b,b)
        
    return es_potencia

#%% Ejercicio 10.5: Subcadenas

def posiciones_de(cadena, subcadena):
    """
    precondicion: recibe como parámetros dos cadenas a y b,
    devuelve: una lista con las posiciones en donde se encuentra b 
    dentro de a.
    """
    def pos_aux(cadena, subcadena, pos=[]):
        if len(cadena) < len(subcadena):
            return
        
        if cadena.endswith(subcadena):
            l_sub = len(subcadena)
            pos.append(len(cadena)-l_sub)    
            pos_aux(cadena[:-l_sub], subcadena, pos)
        else:
            pos_aux(cadena[:-1], subcadena, pos)
        
        return pos
    
    return pos_aux(cadena, subcadena)
    
    
    


l=posiciones_de('Un tete a tete con Tete', 'te')
    
    
    