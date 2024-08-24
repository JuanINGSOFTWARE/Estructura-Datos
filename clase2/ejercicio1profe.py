control=0
cupo= int (input("ingrese cupo"))
while control < cupo :
    valido= input("voleto valido?")
    if valido == "1":
        print ("persona ingresada")
        control= control+1
    else:
        print("persona no ingresa")

print("cupo lleno")
