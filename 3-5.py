#ACTIVIDAD 3.5: Simulación de operaciones bancarias
import random

titular = 'Ignacio'
saldo = random.randint(0, 1000)
activa = True

while True:
    operacion = (input("Elige operación (ingresar, retirar, consultar, cerrar cuenta, abrir cuenta, salir:"))

    match operacion:
        case 'ingresar':
            if activa:
                cantidad = float(input("Intoduce la cantidad a ingresar:"))
                if cantidad > 0:
                    saldo += cantidad
                    print("Se ingreso el dinero. Saldo Actual", saldo)
                else:
                    print("ERROR:La cantidad debe ser mayor que cero.")
            else:
                print("ERROR:La cuenta esta cerrada, no se puede ingresar dinero")

        case 'retirar':
            if activa:
                cantidad = float(input("Introduce la cantidad a retirar:"))
                if 0 < cantidad <= saldo:
                    saldo <= cantidad
                    print("Se ha retirado la cantidad. Saldo Actual", saldo)
                else:
                    print("ERROR:Saldo insuficiente o cantidad invalida")
            else:
                print("ERROR:La cuenta es cerrada, no se puede retirar dinero")

        case 'consultar':
            estado = "activa" if activa else "cerrada"
            print("Titular:", titular)
            print("Saldo:", saldo)
            print("Estado:", estado)

        case 'cerrar cuenta':
            if activa:
                if saldo == 0:
                    activa = False
                    print("Se ha cerrado la cuenta")
                else:
                    print("ERROR:No se puede cerrar por falta de dinero")
            else:
                print("ERROR:La cuenta ya esta cerrada")

        case 'abrir cuenta':
            if not activa:
                activa = True
                saldo = 0
                print("Se abrio la cuenta y su saldo es 0€")
            else:
                print("ERROR: La cuenta ya esta activa")

        case 'salir':
            estado = "activa" if activa else "cerrada"
            print("--ESTADO FINAL DE LA CUENTA--")
            print("Titular:", titular)
            print("Saldo Final:", saldo)
            print("Estado Final:", estado)

            break

        case _:
            print("Operación no reconocida. Intentelo de nuevo")