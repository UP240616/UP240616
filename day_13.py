#Actividad 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numbers if n <= 0]

#Actividad 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [num for sublist in list_of_lists for inner in sublist for num in inner]

#Actividad 3
lista_tuplas = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]

#Actividad 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
info_extendida = [[pais.upper(), pais[:3].upper(), ciudad.upper()] for lista in countries for (pais, ciudad) in lista]

#Actividad 5
lista_diccionarios = [{'country': pais.upper(), 'city': ciudad.upper()} for lista in countries for (pais, ciudad) in lista]

#Actividad 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [f"{nombre} {apellido}" for pareja in names for (nombre, apellido) in pareja]

#Actividad 7
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

ordenada_origen = lambda x, y, m: y - m * x