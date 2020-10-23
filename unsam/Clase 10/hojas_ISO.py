def hoja_A(n):
    '''Precondicion: Recibe un numero N(natural).
    Devuelve: el tamaño en mm de una hoja ISO.'''    
        
    def aux(n, b=1189, h=841):
        
        if n==0:
            return b, h
               
        if n%2 == 0:
            return aux(n-1, b, h//2)
        else:
            return aux(n-1, b//2, h)
        
        
    return aux(n)
