#ACTIVIDAD 3.1: Control de acceso

codigo_secreto = "4826"
MAXIMO_INTENTOS = 3
codigo = ""

while codigo != codigo_secreto and MAXIMO_INTENTOS > 0:
    codigo =input("Introduce el codigo: ")

    match codigo:
        case "4826":
            print("Acceso autorizado")
        case _:
            MAXIMO_INTENTOS = MAXIMO_INTENTOS -1
            if MAXIMO_INTENTOS > 0:
                print("Codigo incorrecto. Quedan", MAXIMO_INTENTOS, "intentos")
            else:
                print("Acceso bloqueado, se agotaron los 3 intentos")