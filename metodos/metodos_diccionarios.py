diccionario = {
    "nombre" : 'nico',
    "apellido" : 'robledo',
    "subs" : 0
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()



#obteniendo un elemento con get(). Si no encuentra nada no lanza una excepción, sino que el programa continua
valor_de_nico = diccionario.get("nombre")
print("Hola jefe")

#eliminando todo del diccionario
#diccionario.clear

#eliminando un elemento del diccionario
diccionario.pop("nombre","subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)