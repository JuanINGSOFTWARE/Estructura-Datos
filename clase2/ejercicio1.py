#crear un sistema de control de ingreso para evitar el sobrecupo 
#definir cual va a ser el numero a controlar
#antes de permitir el ingreso debe solicitar el boleto de entrada
#si el boleto no es balido mostrar el mensaje  "No permitir", de lo contrario dejar entrar y contar el cupo
#cuando el cupo se llene completamente mostrar como mensaje final "no se permite mas ingresos"

boletos=0
print("bienvenido")
C=0
 
while boletos <=10:
        mensaje= int(input("ingrese el numero de su boleto, tenemos asientos de la silla 1 hasta la 10"))
        if mensaje<11:
                print(f"nos quedan {10-boletos}")
                print("bienvenido a su asiento #",mensaje)
                boletos +=1
                
        elif mensaje>10:
                print("no hay asientos disponibles",mensaje)
       





