import random

def jugar():
    print("¡Bienvenido al juego de adivinar el número!")

    while True:
        try:
            dificultad = int(input("Selecciona un rango para el número (por ejemplo, 100 para 1-100): "))
            if dificultad <= 1:
                print("Por favor, elige un rango mayor a 1.")
                continue
            break
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")

    numero_secreto = random.randint(1, dificultad)
    intentos = 0


    while True:
        try:
            intento = input(f"Adivina el número entre 1 y {dificultad}: ")
            
            if intento.lower() == "exit":
                print("Has salido del juego. ¡Hasta luego!")
                break
            
            intento = int(intento)
            intentos += 1
            
            if intento < numero_secreto:
                print("El número secreto es mayor.")
            elif intento > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except ValueError:
            print("Eso no es un número válido. Por favor, introduce un número.")
