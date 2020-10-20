def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2

        if lista[medio]==e:
            res = True
        elif e < lista[medio]:
            res = bbinaria_rec(lista[:medio], e)
        else:
            res = bbinaria_rec(lista[medio+1:], e)
	

    return res

print(bbinaria_rec([1, 2,4,6,7,8,9,11], 3))
print(bbinaria_rec([1, 2,4,6,7,8,9,11], 1))
print(bbinaria_rec([1, 2,4,6,7,8,9,11], 7))