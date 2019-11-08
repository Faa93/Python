def crearListaDesdeArchivo(nombreArchivo):
    archivo = open(nombreArchivo , 'r')
    sale=[ ]
   
    linea = archivo.readline( ).replace('\n', ' ')
    
    while linea!= "":
        linea = linea.split(",")
        sale.append((linea[1],linea[2]))
        linea = archivo.readline( ).replace('\n', ' ')
        
    return sale


def mostrar(lista):
    for x in lista:
        print(x)


#def crearArchivo(provincia, ciudad):
    
    



    
    
def main():
 
    lista = crearListaDesdeArchivo("C:\\Users\\Public\\Localidades.csv")
    
    
    mostrar(lista)
        
    
    
    
    
    
main()