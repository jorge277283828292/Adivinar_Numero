while True:
    try:
        Numero=int(input("Que tabla de multiplicar deseas ver? "))
        if 1 <= Numero <= 12:
            for i in range(1, 10):
                print(f"{Numero} x {i} = {Numero * i}")
        else:
            print("Numero invalido")
    except Exception as e:
        (f"A ocurrido un error ,{e}")
        continue

    Continuar = input("¿Desea ver otra tabla de multiplicar?")
    Continuar = Continuar.lower().strip()
    if Continuar != "si":
        break