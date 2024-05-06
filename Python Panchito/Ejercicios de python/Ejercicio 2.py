

valores = [True, 5, False, "hola", "adios", 2]

if len(valores[3]) < len(valores[4]):
    print(valores[0])
    print("adios es mayor que hola")
else:
    print(valores[2])
    print("no se cumple la condición")

resultado_true = valores[0] or valores [2]
resultado_false = valores[0] and valores [2]

print(resultado_true)
print(resultado_false)

suma = valores[1] + valores[5]
resta = valores[1] - valores[5]
division = valores[1] / valores[5]
multiplicacion = valores[1] * valores[5]

print("Suma",suma)
print("Resta",resta)
print("Division",division)
print("Multiplicacion",multiplicacion)


