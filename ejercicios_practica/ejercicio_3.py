# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"
from turtle import clearscreen


clearscreen
# Dado la siguiente lista de números, utilizar "for"
# para recorrer toda la lista y realizar la sumatoria de todos los números
# La sumatoria se deberá ir guardando en la variable "suma"
i = 0
numeros = [1, 5, -1, 6, 10, 2, -5]
suma = 0   # Variable ya inicializada, la suma arranca en cero
ciclo = len(numeros)
for i in range(ciclo):
    suma = suma + numeros[i]
print("El resultado de sumar los términos de 'numeros' es ",suma)
print("terminamos!, el resultado final almacenado en suma debe ser 18")
