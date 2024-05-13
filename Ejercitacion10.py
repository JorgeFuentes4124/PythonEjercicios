


parciales = float(input("Ingrese la calificación de los exámenes parciales (0-10): "))
practicos = float(input("Ingrese la calificación de los trabajos prácticos (0-10): "))
integrador = float(input("Ingrese la calificación del examen integrador (0-10): "))

# Calcular la contribución de cada aspecto a la calificación final
nota_parciales = parciales * 0.3
nota_practicos = practicos * 0.2
nota_integrador = integrador * 0.5

# Calcular la calificación final sumando las contribuciones de los tres aspectos
calificacion_final = nota_parciales + nota_practicos + nota_integrador

# Imprimir la calificación final
print("La calificación final del estudiante es:", calificacion_final)


























