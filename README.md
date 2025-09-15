# Repo-1-Programación-Orientada-a-Objetos
Solución propuesta por el estudiante Lucas García, a los ejercicios propuestos por el docente en el reto 1. del curso.
***
## Inciso 1.
Una función en donde al ingresar 2 números, y elegir una operación, te entrega el resultado.

Cómo se puede apreciar, además de la función requerida, se agregó la estructura de do-while, en caso de ingresar un valor no válido.
```python
def funcion(a: int, b: int) -> float:
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
                else:
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
