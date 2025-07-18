#Actividad 1 
print("Iterar 0 a 10 usando for:")
for i in range(11):
    print(i, end=' ')
print("\n")
print("Iterar 0 a 10 usando while:")
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print("\n")

#Actividad 2 
print("10 a 0 usando for:")
for i in range(10, -1, -1):
    print(i, end=' ')
print("\n")
print("Iterar 10 a 0 usando while:")
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1
print("\n")

#Actividad 3 
print("Triángulo de hashes:")
for i in range(1, 8):
    print('#' * i)
print("\n")



#Actividad 4 
print("Cuadrícula 8x8:")
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()
print("\n")



#Actividad 5 
print("Cuadrados de números del 0 al 10:")
for i in range(11):
    print(f"{i} x {i} = {i*i}")
print("\n")

#Actividad 6 
print("Elementos de la lista:")
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lista:
    print(item)
print("\n")

#Activida 7 
print("Números pares de 0 a 100:")
for i in range(0, 101, 2):
    print(i, end=' ')
print("\n")

#Actividad 8 
print("Números impares de 0 a 100:")
for i in range(1, 101, 2):
    print(i, end=' ')
print("\n")



#Actividad 1 **************Level 2*******************
suma_total = 0
for i in range(101):
    suma_total += i
print(f"La suma de todos los números de 0 a 100 es {suma_total}\n")

#Actividad 2
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print(f"La suma de los pares es {suma_pares}. La suma de los impares es {suma_impares}\n")



# Actividad 1 ***********level 3 **************
countries = [
    "Finland", "Sweden", "Iceland", "Denmark", "Ireland", "Poland", "Thailand", "Netherlands", "England", "Scotland"
]

print("Países que contienen 'land':")
for country in countries:
    if 'land' in country.lower():
        print(country)
print("\n")

#Actividad 2
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_invertidas = []
for i in range(len(frutas)-1, -1, -1):
    frutas_invertidas.append(frutas[i])

print("Lista invertida de frutas:")
print(frutas_invertidas)
print("\n")

#Actividad 3
countries_data = [
    {'name': 'Finland', 'languages': ['Finnish', 'Swedish'], 'population': 5536146},
    {'name': 'Sweden', 'languages': ['Swedish'], 'population': 10353442},
    {'name': 'Norway', 'languages': ['Norwegian'], 'population': 5421241},
    {'name': 'Denmark', 'languages': ['Danish'], 'population': 5822763},
    {'name': 'Iceland', 'languages': ['Icelandic'], 'population': 366425}
]

idiomas = set()
for country in countries_data:
    for lang in country['languages']:
        idiomas.add(lang)

print(f"Total de idiomas únicos: {len(idiomas)}")
print("\n")

# Actividad 4
from collections import Counter

contador_idiomas = Counter()
for country in countries_data:
    for lang in country['languages']:
        contador_idiomas[lang] += 1

mas_hablados = contador_idiomas.most_common(10)
print("Los 10 idiomas más hablados:")
for idioma, cuenta in mas_hablados:
    print(f"{idioma}: {cuenta} países")
print("\n")

#Actividad 5
paises_ordenados = sorted(countries_data, key=lambda x: x['population'], reverse=True)
print("Los 10 países más poblados:")
for pais in paises_ordenados[:10]:
    print(f"{pais['name']}: {pais['population']}")