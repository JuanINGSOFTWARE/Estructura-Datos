x=int(input("ingrese un numero"))
y=int(input("ingrese un numero"))
z=int(input("ingrese un numero"))

mayor= x
if y>mayor:
    mayor=y
if z>mayor:
    mayor=z
menor = x
if y < menor:
  menor = y
if y < menor:
  menor = z

print("el numero mayor es",mayor)
print("el numero menor es",menor)



