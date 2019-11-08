#23. Una empresa de telefonía nos pide escribir un programa que le brinde información sobre
#el consumo de sus clientes residenciales. Para ello se ingresa, por cada una de las llamadas realizadas en el último mes:
#● Código de Cliente (int de 5 dígitos, entre 10001 y 99999, 0 = fin)
#● Duración de la llamada nro. (int > 0).
#● Tipo de abono (“A”, “B” o “C”).
#Para calcular el importe de cada llamada, nos informan que el costo por minuto, de acuerdo
#al tipo de abono, es el siguiente:
#● Abono “A” => $2 el minuto
#● Abono “B” => Hasta 5 minutos, $2 el minuto; Más de 5 minutos, $1,5 el minuto.
#● Abono “C” => $1 el minuto con un máximo de $10 (Ej. si habla 15 minutos paga $10).
#Se pide informar:
#1. El importe acumulado a recaudar por cada tipo de abono.
#2. La cantidad de minutos de la llamada más larga.
#3. La cantidad de llamadas de menos de 6 minutos.
#4. El precio promedio por llamada.

import random as R

def get_llamada():
  
    cliente  = R.randint(0,1000)
    duracion = R.randint(1,100)
    tipo     = R.randint(1,3)
    
    return(cliente,duracion,tipo)

def main():
    importe = 0
    llamada = get_llamada()
    
    while llamada [0] != 0:
       
        if llamada[2] == 2:
            
            if  llamada  [1] <= 5:
              importe = 2* llamada[1]
            else:
              importe = 10 + (llamada[1] -5) * 1.5
        else:
              
          
            if llamada[2] == 1:
                 importe = 2 * llamada[1]
            else:
                 importe = 10
    
    
    print(llamada, "El importe es: ", importe)
    
    
          
        
main()