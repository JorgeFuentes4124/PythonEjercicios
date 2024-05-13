


salario_base = 5500
comision_por_auto = 200

# Solicitar al usuario el número de autos vendidos y el valor de venta de la unidad
autos_vendidos = int(input("Ingrese el número de autos vendidos: "))
valor_venta_unidad = float(input("Ingrese el valor de venta de la unidad: "))

# Calcular la comisión total por los autos vendidos
comision_total = comision_por_auto * autos_vendidos

# Calcular el adicional del 5% del valor de venta de cada auto
adicional_valor = valor_venta_unidad * 0.05 * autos_vendidos

# Calcular el salario total del vendedor sumando el salario base, las comisiones y los adicionales
salario_total = salario_base + comision_total + adicional_valor

# Imprimir el salario total del vendedor
print("El salario total del vendedor es:", salario_total, "pesos")
















