peso= float(input("ingrese su peso"))
estatura= float(input("ingrese su estatura"))

IMC=peso/(estatura*estatura)

if IMC>25.0:
    print("esta en sobre peso")

else:
    print("su peso es normal")

