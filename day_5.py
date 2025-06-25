#Actividad 1 
lista=list()
print(lista)


#Actividad 2 
lista_1=["lambo","ferrari","jaguar","mclaren","audi","cadilac"]
print(lista_1)


#Actividad 3 
marcas=len(lista_1)
print("el numero de marcas son: ",marcas)


#Actividad 4 
marca_1=lista_1[0]
print(marca_1)
marca_2=lista_1[3]
print(marca_2)
marca_3=lista_1[5]
print(marca_3)


#Actividad 5 
mix_tipos_datos=["Uriel","19","1.75","Soltero","Arco de Belen"]
print(mix_tipos_datos)


#Actividad 6
companias=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]


#Actividad 7
print(companias)


#Actividad 8
print(len(companias))


#Actividad 9
c1=companias[0]
print(c1)
c2=companias[3]
print(c2)
c3=companias[6]
print(c3)

#Actividad 10
print(mix_tipos_datos)


#Actividad 11 
companias.append("intel")
print(companias)


#Actividad 12 
companias.insert(4,"linux")
print(companias)


#Actividad 13
companias.remove("Google")
companias.insert(1,"GOOGLE")
print(companias)


#Actividad 14
list2=["dell","macbook","asus"]
companias.extend(list2)
print(companias)


#Actividad 15
print(companias.index("dell"))


#Actividad 16
companias.sort()
print(companias)


#Actividad 17
lis_rev=["uriel","kimber","erika","neto"]
lis_rev.sort(reverse=True)
print(lis_rev)

#Actividad 18
ke=lis_rev[0:2]
print(ke)


#Actividad 19
recortadas=companias[:10]
print(recortadas)


#Actividad 20
cortada=companias[5:6]
print(cortada)


#Actividad 21
primer=companias[1:]
print(primer)


#Actividad 22
medio=companias[6:]
print(medio)


#Actividad 23
ultima=companias[:11]
print(ultima)


#Actividad 24
all=companias[0:11]
print("borradas: ",all)



#Actividad 25
del companias[0:11]
print(companias)


#Actividad 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
union=front_end+back_end
print(union)


#Actividad 27
full_stack=union 
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)


#LEVEL 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

#2 
print(ages.index(19))

print(ages.index(26))


#3
ages.insert(0,19)
ages.insert(10,26)
print(ages)


#4
print(ages.index(24))
print(ages.index(24))
print((24+24)/2)


#5
promedio=(19+22+19+24+20+25+26+24+25+24)/10
print(promedio)


#6
rango=26-19
print(rango)


#7
paies=["Mexico","Italia","Alemania","España","Suiza","Estados Unidos","COREA"]
centro=paies[len(paies)//2]
print(centro)

#8
n = len(paies)
mid = (n + 1) // 2  

first_half = paies[:mid]
second_half = paies[mid:]

print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)


#9
europa=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
p_uno,p_dos,p_tres,*rest=europa
print("paises escandivados:",rest)