

Salario = 5500
Comision_por_auto = 200
Autos_vendidos = int(input("Ingrese número de autos: "))

precios_autos = []

# Pedimos al usuario que ingrese el precio de cada auto
for i in range(Autos_vendidos):
    precio = float(input("Ingrese el precio del auto {}: ".format(i+1)))
    precios_autos.append(precio)


Comision_total = Comision_por_auto * Autos_vendidos

Valor_Adicional = sum(precios_autos) * 0.5

Salario_total = Salario + Comision_total + Valor_Adicional

print("El salario total del vendedor es", Salario_total, "Pesos")
















