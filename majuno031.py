import random as R
"""
HACER UNA FUNCION QUE QUITE LOS ELEMENTOS REPETIDOS DE UNA LISTA
"""

def desrepetir(lis):
    sinrep = []
    for x in lis:
        if not x in sinrep:
            sinrep.append(x)
    return sinrep

def crearLista(cantidad,desde,hasta):
    x=[]

    for s in range(cantidad):
       
        x.append(R.randint(desde,hasta))
    
    return x

def estaOrdenada(lis):
   
    i = 0
    while i < len(lis)-1:
        if lis[i] > lis[i+1]:
           return False
        i = i+1
    return True

def main():
    lista1 = crearLista(14,199,299)
    lista2 = crearLista(10,199,299)
    lista3 = crearLista(255,1,24)

    print("lista1 ",lista1)
    print("lista2 ",lista2)
    print("lista3 ",lista3)
    lista = ["mama","mame","mami"]
    if estaOrdenada(lista):
        print("si")
    print(lista)
    print(lista3)
    ssss = desrepetir(lista3)
    print(ssss)
    
main()