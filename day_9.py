#Actividad 1 
a=int(input("ingresa tu edad"))
if a >= 18:
    print("tienes edad suficiente para manejar")
else:
    edad= 18-a 
    print("te faltan ",edad,"año(s) para aprender a manejar")


#Actividad 2
tu=int(input("Tu edad:"))
yo=int(input("Mi edad:"))
if tu>yo:
    print("tu eres mas viejo que yo")
elif tu<yo:
    print("yo soy mas viejo que tu")
else:
    print("tenemos la misma edad")


#Actividad 3
num_a=int(input("ingresa un numero:"))
num_b=int(input("ingresa el segundo numero"))
if num_a>num_b:
    print(num_a," es mayor que",num_b)
elif num_a==num_b:
    print("los numeros son iguales")
else:
    print(num_b," es mayor que ",num_a)


#Actividad 1  *********LEVEL 2*************
calif=int(input("ingresa tu calificacion en numero entero:"))
if calif>=80 and calif<=100:
    print("A")
elif calif>=70 and calif<=89:
    print("B")
elif calif>=60 and calif<=69:
    print("C")
elif calif>=50 and calif<=59:
    print("D")
elif calif>=0 and calif<=49:
    print("F")
else:
    print("numero fuera del rango")



#Actividad 2 
temporada=input("Ingresa un mes del año:")
if temporada=="septiembre" or temporada=="octubre" or temporada=="noviembre":
    print("la temporada es otoño")
elif temporada=="diciembre" or temporada=="enero" or temporada=="febrero":
    print("estamos en invierno")
elif temporada=="marzo" or temporada=="abril" or temporada=="mayo":
    print("estamos en primavera")
elif temporada=="agosto" or temporada=="junio" or temporada=="julio":
    print("estamos en verano")



#Actividad 3
fruits = ['banana', 'orange', 'mango', 'lemon']
ingresa=input("ingresa una fruta:")
if ingresa in fruits:
    print("esa fruta ya existe")
else:
    print("la fruta no existe asi que agregamos la fruta")
    fruits.append(ingresa)
    print(fruits)



#Actividad 1 ***********LEVEL 3***************
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person:
    print(person["skills"][2])

# *************** *******************
if "skills" in person:
    if "Python" in person["skills"]:
        print("la habilidad si esta")
    else:
        print("no tiene la habilida")

#**************** *******************

if "skills" in person:
    if "JavaScript" and "React" in person["skills"]:
        print("El es un desarrollador front-end")
    elif "Node" and "Python" and "MongoDB" in person["skills"]:
        print("El es un desarrollador back-end")
    elif "React" and "MongoDB" and "Node" in person["skills"]:
        print("el es un desarrollador full stack")
    else:
        print("titulo desconocido")