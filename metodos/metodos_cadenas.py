cadena1 = "Hola,maquina,soy,Nico"
cadena2 = "Bienvenido jefe"
 #Dato. Metodo ()  => estructura de los métodos

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minúsculas
minusc = cadena1.lower()

#primera letra en mayúsculas
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepción
busqueda_index = cadena1.index("a")

#si es numérico, devuelve true, si no devuelve false
es_numerico = cadena1.isnumeric()

#si es alfanumerico, devuelve true, si no devuelve false
es_alfanumerico = cadena1.isalpha()

#cuenta las coincidencias de una cadena dentro de otra cadena, devuleve la cantidad de veces que conincide, si no hay coincidencias devuelve 0
contar_coincidencias = cadena1.count("a")

#contamoscuantos caracteres tiene una cadena
contar_cadenas = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es así devuelve true
empieza_con = cadena1.startswith("Hola")

#verificamos si una cadena termina con otra cadena dada, si es así devuelve true
termina_con = cadena1.endswith("a")

#reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace(","," ")
cadena_nueva2 = cadena_nueva.capitalize()

#separar cadenas con la cadena que le demos
cadena_separada = cadena1.split(",")


print(cadena_separada[1])