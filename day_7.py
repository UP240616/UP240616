#Level_1
#Actividad 1 
it_companies={"intel","dell","asus","acer","Lenovo"}
uno=len(it_companies)
print(uno)


#Actividad 2 
it_companies.add("twitter")
print(it_companies)


#Actividad 3
varias={"facebook","instagram","tiktok"}
it_companies.update(varias)
print(it_companies)


#Actividad 4 
it_companies.remove("facebook")
print(it_companies)


#Actividad 5 *************FALTA**********************



#LEVEL 2
#ACTIVIDAD 1
a={"asus","dell","lenovo","msi","alien ware"}
b={"intel","ryzen","amd","lenovo"}
union_1=a.union(b)
print(union_1)


#Actividad 2
inter=a.intersection(b)
print(inter)


#Actividad 3
disj=a.isdisjoint(b)
print(disj)


#Actividad 4
union_a=a.union(b)
union_b=b.union(a)
print(union_a)
print(union_b)


#Actividad 5
diferencia=a.difference(b)
diferencia_2=b.difference(a)
print(diferencia)
print(diferencia_2)



#Actividad 6
simetric=a.symmetric_difference(b)
print(simetric)



#Actividad 7
del a 
del b 




#Level_3
#Acitivdad 1 
edades = [18, 21, 18, 25, 30, 21, 25]
longitud=len(edades)



#Actividad 2
print("Una cadena es una secuencia de caracteres (letras, numeros, simbolos)." \
"Una lista es una coleccion ordenada de elementos que si se puede modificar." \
"Una tupla es como una lista, pero no se puede modificar." \
"Un conjunto es una coleccion no ordenada y sin duplicados.")


#Actividad 3
lista_unicas="I am a teacher and I love to inspire and teach people"
unicas=lista_unicas.split()
print(unicas)