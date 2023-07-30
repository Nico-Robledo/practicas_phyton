#creando diccionarios con dict()
diccionario = dict(nombre="Nico",apellido="Robledo")


#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario ={frozenset(["nico","pocho"]): "jajas"}

#crando diccionarios con fromkeys() valor por defecto es none
diccionario = dict.fromkeys("nombre","apellido")

#crando diccionarios con fromkeys() cambiando al valor "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"no se")



print(diccionario)