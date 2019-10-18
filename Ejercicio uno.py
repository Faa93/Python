import random as R
def main():
    
    numUno = R.randint(10000,99999)   
    
    u = numUno % 10
    d = (numUno % 100) // 10
    c = (numUno % 1000) // 100
    um = (numUno % 10000) // 1000
    dm = ( numUno % 100000) // 10000
    
    print(numUno)
    
    invertido = (u * 10000) + (d * 1000) + (c * 100) + ( um * 10) + (dm * 1)

    print("El numero invertido es: ", invertido)
    
    if numUno == invertido:
        print("El numero es capicua")
    
    else:
        print("No capicua")
    
main()

