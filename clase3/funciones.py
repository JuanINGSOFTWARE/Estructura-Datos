# crear una funcion que calcule el factorial de un numero, como parametro de entrada
# debe recicbir numero a calcular

def calcular_factorial(numero=int)->int:
    resultado= 1
    if numero<0:
        return"no se puede valores negativos"
    # podemos omitir este paso 
    # elif numero==0:
        #return
    for n in range(1,numero): 
         resultado= resultado*n
    return resultado

# para llamar una funcion que ya tenemos
#op1
factorial= calcular_factorial(5)
print("El resultado del factorial es",factorial)
#op2
print("El resultado del factorial es",calcular_factorial(5) )



