frutas = ["piesco","sandía","plátano","musicu","pera","fresa","manzana"]
cadena = "Hola Nico"
numeros = [2,5,8,10]

#evitando que se coma un piesco con la sentencia continue

for fruta in frutas:
    if fruta == 'piesco':
       continue
    print(f'Me voy a comer un/una {fruta}')

#evitar que el bucle siga ejecutándose (el else tampoco se ejecuta si hay un break)
for fruta in frutas:
    print(f'Me voy a comer un/una {fruta}')
    if fruta == 'pera' :
        break
else: 
    print("bucle terminado")


#recorrer una cadena de texto

for letra in cadena :
    print(letra) 


#for en una sola linea de codigo
numeros_duplicados = [x+2 for x in numeros]

print(numeros_duplicados)