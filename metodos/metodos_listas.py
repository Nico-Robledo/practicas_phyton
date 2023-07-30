#Creando una lista con list()

lista= list([ 33, 56, True, False])

#devuleve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#añadiendo un elemento a la lista
lista.append(65)

#añadiendo un elemento a la lista en un indice específico
lista.insert(2,"TOMA MAMA")

#añadiendo varios elemEnetos a la lista
lista.extend([False,2023])

#eliminando un elemento de la lista por su indice. Si se pone el inidce -1 se borra siempre el último elemento; el -2 borra el penúltimo y así sucesivamente
lista.pop(3)

#quitando un elemento de la lista por su valor
lista.remove("TOMA MAMA")

#ordenando la lista de forma ascendente, si usamos el reverse = True lo ordena a la inversa
lista.sort(reverse=True)

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(56)




#eliminando todos los elementos de la lista
#lista.clear()

print(dir(set(["dihifdhj,yhfeuygfe"])))