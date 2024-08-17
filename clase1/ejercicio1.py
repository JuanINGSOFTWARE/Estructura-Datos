x=int(input("ingrese un numero"))
y=int(input("ingrese un numero"))
z=int(input("ingrese un numero"))

mayor= x
if y>mayor:
    mayor=y
if z>mayor:
    mayor=z
menor = x
if y < mayor:
  menor = y
if z < menor:
  menor = z

print("el numero mayor es",mayor)
print("el numero menor es",menor)



