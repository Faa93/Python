from time import time
import random as R

def crearUnArchivoRandom(nombreArchivo,tamanio,desde,hasta):
    archivo = open(nombreArchivo,'w')#ABRIMOS PARA ESCRITURA (CREAR UN ARCH. NUEVO)

    for i in range(tamanio):
        archivo.write(str(R.randint(desde,hasta)) + "\n")

    archivo.close()

def leerDesdeArchivo(nombreArchivo):
    lista=[]
    archivo = open(nombreArchivo,'r')

    linea = archivo.readline()
    while linea != "":
        lista.append(int(linea))
        linea = archivo.readline()
    archivo.close()
    return lista
    ordenar(lista)
    #guardarEnArchivo("ordenados.txt",lista)

def ordenar(lista):#BURBUJA
    for i in range(0,len(lista)-1):
        for d in range(i+1,len(lista)):
            if lista[i] > lista[d]:
                aux      = lista[i]
                lista[i] = lista[d]
                lista[d] = aux


def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
        return lista





def main():
    #crearUnArchivoRandom("C:\\Users\\ITMaster\\Desktop\\pythonmajuno\\numeros.txt",20000,1,1000)
    lista = leerDesdeArchivo("C:\\Users\\ITMaster\\Desktop\\pythonmajuno\\numeros.txt")
    principio = time()
    #sort(lista)
    sorted(lista)
    fin = time() 
    
    
    print("TIEMPO: " ,fin-principio)
    #guardarEnArchivo("ordenados.txt",lista)
    #print(lista)

main()