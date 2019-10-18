def main():
    
    
    fecha = int(input("Ingrese AAAAMMDD: "))
    
    
    
    dia = fecha % 100
    mes =(fecha % 10000) //100
    año = fecha // 10000
    
    
    fecha = str(dia) + "/" + str(mes) + "/" + str(año)
    
    print(fecha)
    
    
    
    
    
main()