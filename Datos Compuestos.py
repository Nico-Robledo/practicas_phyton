
#creando una lista modificable
lista=["Nico", "14 años", True, 1.81]

#creando una lista no modificable
tupla=("Nico", "14 años", True, 1.81)

#esto es válido
lista[3]= 2.06

#esto no
#tupla[3]=2.06

#creando un conjunto (set), no se puede nombrar a los elementos por su índice y no almacena datos duplicados
conjunto={"Nico", "14 años", True, 1.81}

#print(conjunto[3])--- no se puede acceder al elemento


#creando un diccionario (dict) la estrucutra es key : value y separamos con comas
diccionario= {
    'nombre'  :"Nico Robledo",
    'edad' : "14 años",
    'le_gusta_programar' : True,
    'altura': 1.82,
    'dato_duplicado':"Nico Robledo"
    }
print(diccionario['altura'])
print(lista[0])