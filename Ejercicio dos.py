"""
japones u+d == c-um
coreano d == c+u
chino d-c == um + dm

superchino es la combinacion de todos
"""


import random as R

def main():
    
    numeroRandom = R.randint(10000,99999)
    
    u = numeroRandom % 10
    d = (numeroRandom % 100) // 10
    c = (numeroRandom % 1000) // 100
    um = (numeroRandom % 10000) // 1000
    dm = (numeroRandom % 100000) // 10000
    
    cartel= ""
    flag = 0

    if u+d == c-um:
        cartel= cartel + " Es re japones "
        flag = flag + 1
        
    if d == c+u:
        cartel= cartel + " Es re coreano "
        flag = flag + 1
    
    if d-c == um+dm:
        cartel= cartel + " Es re chino "
        flag = flag + 1
        
    if flag == 3:
        cartel ="¡¡¡¡¡Es super chino!!!!!!"
        
    
    print("Su numero es: ", numeroRandom, cartel)
    

main()