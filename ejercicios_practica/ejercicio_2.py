# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"
from turtle import clearscreen

clearscreen
# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores
colores = ['rojo', 'naranja', 'verde', 'azul']
color = len(colores)
x = 0
# Itere el "for" utilizando la lista como parámetro
# y utilizar como elemento del "for" cada color
# for color ...
for x in range(color):
    print(colores[x])
# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...

print("terminamos!")