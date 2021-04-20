# Ejemplo0:

## Crear una lista con un bucle for:
'Numeros del 1 al 20'
lista_num = list()

'con el range le decimos que itere numerosen orden del 1 al 21 ya que no toma el nuemro final'
for i in range(1,21,1):
  lista_num.append(i)

## vamos a aplicar una opereción sobre la lista:

cambio = [] # otra manera de definir una lista

for n in lista_num:
  cambio.append(n*n)

print(cambio)

"eliminamos nuestra lista de operaciones"
del(cambio)
## Ahora veamolo con listas por compresión:

cambio = [n*n for n in lista_num] # un  mejor zen de python

'''
Obteniéndose el mismo resultado solamente con mucho menos código.
En el código los corchetes indican que la salida de la lista n*n es la expresión que ejecutar para cada uno de los elementos del bucle for.
Es decir, que a cada uno de los valores sobre los que se itera se multiplique por ella misma.
'''

## Veamos los cambios que efectuamos
print(cambio)

# Condicionales con compresión:
cambio_if = [n*n for n in lista_num if n*n <= n *2]

'''
Al ejecutar el código se puede observar que solamente se tienen dos registros, los que cumple la condición.
es decir itera los numeros multiplicados por ellos y guarda en la lista si cumple la condicción n*n <= n * 4
'''

## veamos los resultados:

print(cambio_if)

## Ahora un if con un else:
docs = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero', 'Hola', 'Mundo', 'Daniel villa']

'''
Aqui lo que hacemso es llmar a una lista donde tenemos
almacenados nombres dde doctores, los cuales si cumplen la condición de anteponer Dr.
en el str, seran dejados igual, pero sino se les agregara un texto diciendo 'No soy Doctor'
'''

dr = [x if 'Dr.' in x else ('No soy Doctor') for x in docs]

## Veamos resultados:
print(dr)

# Dos for:
'''
Vamos a buscar los nuemros iguales en una lista:
'''
from random import randint

'''
Definimos con la funcion randint de la libreria random
10 numeros aletorios del 1 al 20
'''
numeros1 = [randint(1,20) for x in range(10)]

numeros2 = [randint(1,20) for x in range(10)]


'''
con bucles anidados podemos decirle que si x == y, x => numeros de numeros1
& y=> nuemros de numeros2

así imprimira el resutlados de su igualdad
'''
en_comun = [x for x in numeros1 for y in numeros2 if x == y] 

# Veamos que imprime:
print(en_comun)