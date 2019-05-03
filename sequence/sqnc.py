"""Nuestro breve diccionario de secuencias"""

#Por iteración, por recursión. 


#Los primeros mil elementos en N. 
for n in range(1,100):
    print(n)

#Los mil primeros números pares. 
for p in range(1,100): 
    print(2p)

#Los primeros mil números cuadrados. 
for s in range(1,100):
    print(s ** 2)

#Los números triangulares. 
for n in range(1,100): 
    m = n * (n + 1)
    t = m / 2
    print(t)

#Por recursión

#Los números Fibonacci

f0 = 0
f1 = 1

print(f0, f1)

for i in range(2,100): 
   fn = f0 + f1
   f0 = f1
   f1 = fn
   print(fn)

 




 
    





