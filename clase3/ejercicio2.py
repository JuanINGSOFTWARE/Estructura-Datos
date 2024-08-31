#crear una funcion que convierta temperatura celcius a farenheit
def calcular_temperatura(temperatura):
    resultado = ((temperatura*9)/5)+32
    return resultado
    
try:
     temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
     temperatura_fahrenheit = calcular_temperatura(temperatura_celsius)
     print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit:.2f}")
except ValueError:
     print("Error: Ingresa una temperatura válida (número).")