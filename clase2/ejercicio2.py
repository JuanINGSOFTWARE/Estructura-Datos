#almacenar en un arreglo llamado pares todos los numeros pares hasta el 100
pares=[]
for i in range(1,100):
    if i%2==0:
      pares.append(i)

print(pares)