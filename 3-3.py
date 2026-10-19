#ACTIVIDAD 3.3: Maquina expendedora

precio_producto = 170
monedas_validas = [10, 20, 50, 100]
importe_total = 0

while importe_total < precio_producto:
    moneda = int(input("Introduce una moneda valida: "))

    if moneda in monedas_validas:
        importe_total = importe_total + moneda
        print("Importe acumulado:", importe_total, "centimos")
    else:
        print("No se acepta esta moneda. Introduzca una valida")

cambio_centimos = importe_total - precio_producto
cambio_euros = cambio_centimos / 100

print("Cambio a devolver en céntimos:", cambio_centimos)
print("Cambio a devolver en euros:", cambio_euros, "€")
