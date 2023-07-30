animales = ["iguana","perro","gato","loro","caimán"]
numeros = [2,15,58,0,12]

#recorriendo la lista animales
for animal in animales :
    print(f'Ahora la variable animal es igual a: {animal}')


#recorriendo la lista números y multiplicando cada valor por diez
for numero in numeros :
    resultado = numero * 10 
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo

for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')


#forma no óptima de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
   print(numeros[num])



#forma correcta de recorrer una lista con su índice
for num in enumerate(numeros):
    indice = num[0]
    valor = num [1]
    print (f'el indice es: {indice} y el valor es : {valor}')


#usando el for/else
for numero in numeros:
    print(f"ejecutando el último bucle, balor actual: {numero}")
else:
    print("el bucle terminó")


#todo lo anterior funciona igual con tuplas y conjuntos