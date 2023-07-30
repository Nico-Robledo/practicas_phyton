
#le pedimos al usuario que nos diga una frase (o varias)
frase = input("Dime una frase jefe y te calculo cuanto tardarías en decirla: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos qque hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tardara mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
  print("Hermano, no pongas una biblia")
  
#Calculamos cuanto tardaría en decir  la palabras y se lo decimos
print(f'Dijiste{cantidad_de_palabras} palabras y tardarías en decirlo {cantidad_de_palabras / 2} segundos')
print(f'Dalto lo diría en {cantidad_de_palabras * 100// 2 * 1.3 / 100} segundos')