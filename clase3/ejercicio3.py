#verificar si una palabra dada es un palindromo
def palindromo(palabra:str)->str:
    txt= f"{palabra}"[::-1]
    if palabra == txt:
         return "La palabra es un palindromo" 
    else:
         return"la palabra no es un polindromo"
    
palabra=str(input("Digite la palabra--"))    
print(palindromo(palabra))


