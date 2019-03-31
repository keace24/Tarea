def multiplicar(lista):
    if isinstance (lista,list):
        return multiplicar_aux(lista,0)
    else: return "Error:No introdujo una lista"

def multiplicar_aux(lista,indice):
    if lista==[]:
        return[]
    elif ([lista[0]*indice]):
        return ([lista[0]*indice])+multiplicar_aux(lista[1:],indice+1)
    else: return multiplicar_aux(lista[1:],indice+1)
        
