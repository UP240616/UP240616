#actividad 1
edad=19                                                                 #declaro mi edad 

#actividad 2
mi_altura=1.70                                                          #declaro mi altura

#actividad 3
numero_complejo=4j                                                      #declaro el numero complejo

#actividad 4
altura=float(input("ingresa la altura de un triangulo"))                #pido al usuario agregar la altura del triangulo
base=float(input("ingresa la base del triangulo"))                      #pido al usurio ingrese la base del triangulo  
area=0.5*altura*base                                                    #calculo el area  
print(area)                                                             #muestro el resultado

#actividad 5

lado_a=float(input("Ingresa el lado a del triangulo"))                  #pido al usuario agregar los lados del triangulo
lado_b=float(input("inrgresa el Lado c del triangulo"))                 #pido al usuario agregar    
lado_c=float(input("ingresa el lado c del triangulo"))                  #pido al usuario agregar 
perimetro=lado_a+lado_b+lado_c                                          #calculamos el perimetro
print(perimetro)                                                        #mostramos



#Actividad 6
largo=float(input("Ingresa el largo de un rectangulo")) 
ancho=float(input("Ingresa el ancho de un rectangulo")) 
area_rec=largo*ancho
perimetro_rec=2*(largo+ancho)
print(area_rec,perimetro_rec)

#Actividad 7
radio_cir=float(input("Radio de un cicrulo"))
area_cir=3.14*radio_cir*radio_cir
circunferencia=2*3.14*radio_cir
print(area_cir)

#Actividad 8

x=float(input("ingresa el valor de x"))
y=(2*x)-2
print(y)

m=(y**2) - (y**2)/x**2-(x**2) 
print(m)

#Actividad 9
x1=2
y1=2
x2=6
y2=10
dist_eucl=((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(dist_eucl)

#Actividad 10

if m==dist_eucl:
    print("son iguales")
else:
    print("no son iguales")

#actividad 11
x_1=10
y_1= x**2 + 6*x + 9
print(y_1)

#actividad 12
len_python = len("python")
len_dragon = len("dragon")
print(len_python, len_dragon)

#actividad 13 
print('on' in 'python' and 'on' in 'dragon')


#actividad 14
s1= "I hope this course is not full of jargon"
print('jargon' in s1)

#actividad 15
drag="dragon"
pyt="python"

w1="on" in drag
w2="on" in pyt
print(w1," ",w2)

# actividad 16
py= len("python")
flota=float(py)
cad=str(flota)


#actividad 17

par=int(input("agrega un numero"))

if par % 2 == 0:
    divisible = par/2
    print("es par y su division entre dos es:", divisible)
else:
    print("el numero es impar")


#actividad 18

div_piso= 7//3==int(2.7)
print(div_piso)


#actividad 19

es_igual= type("10")==type(10)
print(es_igual)

#actividad 20
es_dif=type("9.8")==type(10)
print(es_dif)

#actividad 21
horas_t=float(input("ingresa el tiempo que trabajo"))
tarifa=float(input("ingresa la tarifa por hora"))
sueldo=horas_t*tarifa
print("el sueldo sera de: ",sueldo)

#actividad 22
años=int(input("ingresa los años de la persona para saber cuantos segundos vivio "))
al_dia=60*1440
año=al_dia*365
segundos_vida=año*años
print(segundos_vida)

#actividad 23
for i in range(1, 6):
    print(i, 1, i, i*2, i**3)









