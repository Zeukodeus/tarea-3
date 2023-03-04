N = int(input("Ingrese un número de cuatro digitos y positivo: "))

if N<0 :
    rta = "no es positivo"

else :
    if 10000>N>999 :
        rta = "no es positivo pero si es de 4 digitos"

    else :
        rta = "no es positivo ni de 4 digitos"

if N>0 :
    rta = "es positivo"

else :
    if 10000>N>999 :
        rta = "es positivo y de 4 digitos"
    else :
        rta = "es positivo pero no es de 4 digitos"

print (rta)
    