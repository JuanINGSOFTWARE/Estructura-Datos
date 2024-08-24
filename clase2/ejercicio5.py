#crear un arreglo con 10 numeros aleatorios imprimir el promedio de estos numeros
import random
suma=0 
    
for i in range(1,11):
      numero = random.randint(1,30)
      print(numero)
      suma += numero

prom = (suma/10)
print("el promedio de los numeros es",prom)
      
