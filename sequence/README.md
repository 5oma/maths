# Secuencias

En matemáticas, una secuencia es un conjunto numerado de objetos
en el que las repeticiones están permitidas. Como un conjunto, 
contienen miembros (también llamados elementos, o términos). 
El número de elementos (posiblemente infinito) define la longitud
de la secuencia. A diferencia del conjunto, los mismos elementos
pueden aparecer múltiples veces en diferentes posiciones de la secuencia, 
y el orden importa. Formalmente, una secuencia puede ser definida como
una función cuyo domino es el conjunto de los números naturales
(para secuencias infinitas) o el conjunto de los primeros n números
naturales (para una secuencia de longitud finita n). 

En computación, secuencias finitas son llamadas cuerdas o listas. 
Los nombres varían de acuerdo a la manera en que se representan
en la memoria de la compuradora; secuencias infinitas son llamadas
corrientes (streams).

#Reglas para jugar el juego de las secuencias

Algunas reglas para jugar secuencias,

1. Cuando un símbolo ha sido elegido para denotar una secuencia, 
el elemento n de la secuencia es denotado por este símbolo
junto con n como súbindice. Por ejemplo, Fn denota el elemento n
de la secuencia Fibonacci. 

2. Podemos crear una secuencia definiendo sus elementos. 
En la forma de una lista, por ejemplo. 

L = (1, 2, 3, 4)

Para el caso infinito, 

E = (1, 2, 3, 4, ...)

# Una forma de crear una secuencia en python.

Podemos crear una lista

l = [1, 2, 3, 4]

Pero para secuencias más laboriosas, que no
podemos escribir su lista, tenemos que programar
que se genere. 

Veamos, con el siguiente código podemos generar
muchos tipos de secuencias. 


for n in range (1,10): 
     print(n)

Lo que nos arroja como output

>>>
1
2
3
4
5
6
7
8
9
10


Pero, a partir de esta secuencia podemos generar
otras más interesantes. 

for n in range(1,10): 
    print(2 * n + 1)

Este conjunto de scripts producen secuencias.
 
Algunas secuencias que queremos poner aquí.
 

La secuencia de números primos. 
Fibonacci
La secuencia de Cauchy

Una intro a las secuencias mediante el módelo fórmula. 

La secuencia de los números pares puede ser definida así: 

(2n)nEN


En python: 

```python
for n in range(1,1000):
    print(n * 2)
```


La secuencia de los números cuadrados puede ser así: 
(n2)nEN

```python
for n in range(1,1000):
    print( n ** 2)
```

Otra manera, por recursión. 

Por ejemplo, la secuencia fibonacci. 

¿Más info?

En htttps://en.wikipedia.org/wiki/Sequence


 


