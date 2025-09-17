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


if __name__ == '__main__': # Función main para iniciar el código
    Mismos_Caracteres()