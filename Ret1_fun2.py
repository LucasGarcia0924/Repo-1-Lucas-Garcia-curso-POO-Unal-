def palindromo(): # Función requerida
    # Se declaran e inicializan las variables
    letras_normales : list = []
    letras_invertidas : list = []
    Palabra = str(input("Ingrese una palabra para verificar si es un palíndromo:"))

    # Se convierte la palabra a minúsculas para que la mayúscula inicial no afecte la comparación
    Palabra = Palabra.lower()

    # Se llena la lista con las letras en orden normal e invertido
    for letra in Palabra:
        letras_normales.append(letra)
    for i in range((len(letras_normales)), 0, -1):
        letras_invertidas.append(letras_normales[i-1])

    # Se comparan las listas para determinar si la palabra es un palíndromo
    if letras_normales == letras_invertidas:
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")

if __name__ == '__main__': # Función main para iniciar el código
    palindromo()
