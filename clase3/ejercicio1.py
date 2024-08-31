#crear una funcion que realice operaciones basicas(suma,resta....) entre dos numeros

#numero1= int(input("ingrese primer numero"))
#numero2= int(input("ingrese segundo numero"))
     
##calcular= str(input("que operacion quieres hacer?",opciones))

#def opciones(num1,num2)->int:
    # suma= num1+num2
     #resta= num1-num2
     #multiplicacion= num1*num2
     #division=num1/num2

def suma(a, b):
     return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1/2/3/4/5): ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Ingresa números válidos.")
        continue

    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida. Inténtalo de nuevo.")


