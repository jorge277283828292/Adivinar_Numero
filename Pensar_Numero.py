import random as r

print("Piensa en un numero entre 1 y 100. Yo tratare de adivinarlo")

Adivinar = r.randint(1, 100)
Intentos = 1

while True:
    Intentos +=1
    print(f"¿Es {Adivinar} tu numero?") 
    Respuesta = str(input("Ingresa 'Mayor', 'Menor', 'Correcto': "))
    Respuesta_Min = Respuesta.lower()

    if Respuesta_Min == "mayor":
        Adivinar = r.randrange (Adivinar, 100)
        

    elif Respuesta_Min == "menor":
        Adivinar = r.randint(1, Adivinar)

    elif Respuesta_Min == "correcto":
        print(f"¡Adivine tu numero {Adivinar} en {Intentos} intentos!")
        break

    else:
        Intentos +=1
        print("Respuesta no valida. Ingresa 'Mayor', 'Menor', o 'Correcto'.")
        