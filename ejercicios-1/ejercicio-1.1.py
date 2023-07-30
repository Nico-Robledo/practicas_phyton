#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5











#Diferencia de duración

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 10000 // otros_cursos_max / 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100


#Calculando el porcentaje de tiempo vacío removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


#Mostrando las dieferencias de duración (Ejercicio A)
print("----------------------")
print("El cuso de Dalto dura:")
print(f' - un {diferencia_con_min}% menos que el más rápido')
print(f' - un {diferencia_con_max}% menos que el máslento')
print(f' - un {diferencia_con_promedio}% menos que el promedio')
print("----------------------")

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso pormedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso eliminó el {tiempo_vacio_dalto}% de tiempo vacio') 
print("----------------------")

#Mostrando dieferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otos cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de el curso de Dalto')
print("----------------------")