def busqueda(lista,numero,primero,ultimo):
    if ultimo<primero:
        return False
    mitad = (primero+ultimo)//2
    if lista[mitad]==numero:
        return mitad
    elif lista[mitad]<numero:
        return busqueda(lista,numero,mitad+1,ultimo)
    else: return busqueda(lista,numero,primero,mitad-1)
