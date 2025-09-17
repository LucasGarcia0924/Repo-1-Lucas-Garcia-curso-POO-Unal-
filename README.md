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
***
## Inciso 3.
Se pide una función capaz de registrar una lista de números y mostrar cuáles de estos son primos.

Esto se lleva a cabo utilizando el ciclo for, debido a que, al ingresar los números en la primera lista, se itera entre ellos y los que cumplan las condiciones se guardan dentro de la lista de números primos, la cuál, se imprime al final.

De manera específica, las condiciones son:
- Si es menor a 2, no es número primo, se sabe porque 0 y 1 no lo son.
- Si es igual a 2, se guarda; esto es una condición extra ya que, el 2 pese a ser primo, no cumple el condicional siguiente.
- Si es mayor a 2, se divide el número por todos los números entre el 2 y 1 entero más que su mitad debido a que sabemos que los divisores van "en parejas", desde 2 y la mitad y luego haber pasado esta, no es necesario comprobar más si lo dividen completamente, pues ya se habrá revisado "su pareja". De forma que si ningún módulo de estas operaciones es igual a 0, el número es primo.
  
```python
def primos(): # función requerida
    # Declaración e inicialización de variables
    lista_numeros : list = [] 
    lista_primos : list = [] 
    
    # Se pide la lista de números al usuario
    print("Ingresa números enteros para hallar primos (Presiona Enter para finalizar)\n")
    while True: # Ciclo infinito, se rompe con el break
        try:
            lista_numeros.append(int(input("Ingresa un número: \n")))
        except ValueError: # Cuando se ingresa un valor no numérico, se rompe el ciclo
            break

    # Se verifica cuáles números son primos
    for i in lista_numeros:
        if i < 2: # Los números menores a 2 no son primos
            continue
        elif i == 2: # El 2 es primo pero no cumple el próximo condicional
            lista_primos.append(i)
        else:
            # Si el número es divisible por otro entre 2 y su mitad, pasa al siguiente
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else: # Si no se encontró ningún divisor, se agrega a la lista de números primos
                lista_primos.append(i)
    
    # Se itera por los elementos de la lista de números primos para mostrarlos
    print("\nLos valores ingresados que hacen parte de los números primos son:\n")
    for num in lista_primos:
        print(f"{num}")
```
***
## Inciso 4.
Se pedía hallar la mayor suma consecutiva de parejas de números.

Para esto, primero se pedían los números al usuario, luego se hacían las sumas de los números contiguos y se almacenaban en una lista; lista que al ordenarla ascendetemente, permitía tomar el último valor, siendo este el mayor.
```python
def mayor_suma(): # función requerida
    
    # Declaración e inicialización de variables
    lista_numeros : list = [] 
    lista_sumas : list = [] 
    suma: int = 0 
    valor_viejo: int = 0

    # Se pide la lista de números al usuario
    print("Ingresa números enteros para determinar la mayor suma posible")
    print("(Presiona Enter para finalizar)\n")
    while True: # Ciclo infinito, se rompe con el break
        try:
            lista_numeros.append(int(input("Ingresa un número: \n")))
        except ValueError: # Fin del ciclo al ingresar un valor no numérico
            break
    
    # Se calculan las sumas de números consecutivos y se almacenan en una lista    
    for num in range(1, len(lista_numeros)): 
        suma = lista_numeros[num-1] + lista_numeros[num]
        lista_sumas.append(suma)
        suma = 0
    
    # Se ordenan las sumas de menor a mayor
    for i in range(1, len(lista_sumas)):
        for j in range(0, len(lista_sumas)):
            if lista_sumas[i] < lista_sumas[j]:
                valor_viejo = lista_sumas[i]
                lista_sumas[i] = lista_sumas[j]
                lista_sumas[j] = valor_viejo
                valor_viejo = 0

    # Se muestra la mayor suma posible
    print(f"\nLa mayor suma posible es: {lista_sumas[-1]}")
    print(f"Estos fueron los resultados obtenidos: {lista_sumas}")
```
***
## Inciso 5
Se requería una función, que al ingresar una lista de palabras, retorne aquellas con igual caracteres.

En un ciclo while, se ingresan las palabras en una lista, hasta que el usuario presione ENTER, cada palabra se vuelve una lista y se ordena alfabeticamente, para luego comparar estas listas, y si concuerdan, se agregan a un diccionario donde para cada palabra, hay una lista con palabras con sus mismos caracteres.
```python
def Mismos_Caracteres():
    # Declaración de variables
    dicc_conjuntos : dict = {}
    lis_lis_palabras : list = []
    palabra_lista : list = []
    lista_palabras : list = []
    lista_parejas : list = []

    print("Ingresa palabras para comparar si tienen los mismos caracteres")
    print("(Presiona Enter para finalizar)\n")
    while True: # Ciclo para ingresar palabras
        palabra_lista = []
        palabra = str(input("Ingresa una palabra: \n"))
        if palabra == "":
            break
        palabra = palabra.lower()
        for i in palabra:
            palabra_lista.append(i)
        lista_palabras.append(palabra)
        lis_lis_palabras.append(palabra_lista)
    
    # Creación del diccionario con las palabras que tienen los mismos caracteres
    for i in range(len(lis_lis_palabras)):
        for j in range(len(lis_lis_palabras)):
            if lis_lis_palabras[i] == lis_lis_palabras[j]:
                continue
            else:
                if (sorted(lis_lis_palabras[i])) == (sorted(lis_lis_palabras[j])):
                    print(sorted(lis_lis_palabras[i]), sorted(lis_lis_palabras[j]))
                    lista_parejas.append((lista_palabras[j]))
        dicc_conjuntos[lista_palabras[i]] = lista_parejas
        lista_parejas = []

    # Mostrar resultados
    print("Para cada palabra, estas son las que tienen los mismos caracteres:")
    for clave in dicc_conjuntos:
        print(f"{clave} : {dicc_conjuntos[clave]}")
```
