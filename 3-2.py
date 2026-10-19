#ACTIVIDAD 3.2: Comprobar si un número es primo

numero = int(input("Introduce un numero entero mayor que 1: "))

for primo in range(2, numero):
    if numero % primo == 0:
        print("El numero", numero, "no es primo.")
        break
    else:
        print("El numero", numero, "es primo.")