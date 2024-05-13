


Salario = 5500

Comision_por_auto = 200
   
Autos_vendidos = int(input("ingrese número de autos"))
valor_por_unidad = float(input("Ingrese numero del valor de venta por unidad"))

Comision_total = Comision_por_auto* Autos_vendidos

Valor_Adicional = valor_por_unidad* 0.5 * Autos_vendidos

Salario_total = Salario + Comision_total + Valor_Adicional

print("El salario total del vendero es",Salario_total,"Pesos")














