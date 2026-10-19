#Actividad 3.4: Control de aforo de una sala

aforo_limite = 8
aforo_actual = 0

while True:
    accion = input("Introduce una accción:(entra, sale, fin):").strip()

    match accion:
        case 'entra':
            if aforo_actual < aforo_limite:
                aforo_actual += 1
                print("Aforo actual:", aforo_actual)
            else:
                print("La sala esta llena")

        case 'sale':
            if aforo_actual > 0:
                aforo_actual -= 1
                print("Aforo actual:", aforo_actual)
            else:
                print("La sala esta vacia")

        case 'fin':
            print("Ya no se admiten mas entradas ni salidas")
            print("Total de personas en la sala:", aforo_actual)
            break

        case _: 
            print("No se reconoce la accion.")