# Repo-1-Programación-Orientada-a-Objetos
Solución propuesta por el estudiante Lucas García, a los ejercicios propuestos por el docente en el reto 1. del curso.
***
## Inciso 1.
Una función en donde al ingresar 2 números, y elegir una operación, te entrega el resultado.

Se trabajó con la estructura if-else para la selección de casos de la operación deseada, sin embargo, otra opción sencilla era con match-case, ambas opciones permiten al usuario elegir la operación al comparar la variable con un valor dado, en este caso, números enteros del 1 al 4.

Cómo se puede apreciar, además de la función requerida, se agregó la estructura de do-while, en caso de ingresar un valor no válido, repitiendo el ciclo hasta que el valor ingresado sea un número.
```python
def operaciones(): # Función requerida
    # Declaración e inicialización de variables
    a = int(input("Digita el primer valor:"))
    b = int(input("Digita el segundo valor:"))
    num : float = 0
    bandera: bool = True
    print("Elige la operación a realizar:")
    
    while bandera == True:
        try: # Ciclo ideal, se rompe con el cambio en la bandera
            operacion =int(input("Sumar (1), Restar (2), Multiplicar (3) o Dividir (4)"))
            if operacion == 1:
                num = a + b
            elif operacion == 2:
                num = a - b
            elif operacion == 3:
                num = a * b
            elif operacion == 4:
                if b != 0:
                    num = a / b
                else: # Se le indica al usuario cuando la división no se puede realizar
                    print("Error: División por cero no permitida.")
            else:
                print("Elección no válida. Intenta de nuevo.")
                continue
            bandera = False
        except ValueError: # Caso de error por si se agrega un valor inválido
            print("Error: Entrada inválida. Por favor ingresa un número entero")
            continue
    # Se entrega el resultado final
    print(f"El resultado de la operación es: {num}")
```

***
## Inciso 2.
Se necesita una función que valide si una palabra es palíndromo, es decir, que se pueda leer de igual forma en ambos sentidos.

Para lograr esto, primeramente se registra la palabra que desee verificar el usuario, luego, en un ciclo for se recorre la palabra y se guarda en una lista letra por letra.
En otro ciclo, se toma la lista anterior, y se guardan las letras en orden inverso, así, se compara el contenido de ambas listas y si es igual, se le indica al usuario que la palabra sí es un palíndromo; en el caso contrario, se le indica la negativa.
```python
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
```
