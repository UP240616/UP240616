#Actividad 1 

fw="treinta"
sw="dias" 
tw="de"
cw="python"
space=" "
concatenacion= fw + space + sw + space + tw + space + cw
print(concatenacion)


#Actividad 2           
cod="codificacion"
pa="para"
to="todos"
con_2=cod+space+pa+space+to
print(con_2)


#Actividad 3 

empresa=con_2


#Actividad 4
print(empresa)


#Actividad 5
print(len(empresa))


#Actividad 6 
print(empresa.upper())


#Actividad 7 
print(empresa.lower())


#Actividad 8
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())


#Actividad 9 
sin_cod= empresa[12:23]
print(sin_cod)


#Actividad 10
ine="codificacion"
if empresa.find(ine) == 0:
    print("si existe la palabra")
else:
    print("no existe")


#Actividad 11
print(empresa.replace("codificacion","python"))


#Actividad 12
empresa_2=empresa.replace("codificacion","python")
empresa_3=empresa_2.replace("todos","all")
print(empresa_3)

#Actividad 13
print(empresa_2.split())


#Actividad 14
redes="facebook\tGoogle\tMicrosoft\tApple\tIBM\tOracle\tAmazon"
print(redes.expandtabs(2))


#Actividad 15
print(empresa[0])


#Actividad 16
sub_string="s" 
print(empresa.index(sub_string))


#Actividad 17
print(empresa[10])


#Actividad 18                               #python para todos
l1=empresa_2[0]                               #01234567890123456789212
l2=empresa_2[7]
l3=empresa_2[12]
union=l1+l2+l3
print(union.swapcase())


#Actividad 19                               #codificacion para todos
l1=empresa[0]                               #01234567890123456789212
l2=empresa[13]
l3=empresa[18]
union=l1+l2+l3
print(union.swapcase())


#Actividad 20
letra_c="c"
print(empresa.index(letra_c))


#Actividad 21
letra_f="f"
print(empresa.index(letra_f))


#Actividad 22
print(empresa_3.rfind("l"))


#Actividad 23
word="No puedes terminar una oracion con because porque because es una conjuncion"
print(word.find("because"))


#Actividad 24
print(word.rindex("because"))


#Actividad 25
sentence=word.replace("because porque because", "")
print(sentence.strip())


#Actividad 26
print(word.find("because"))


#Actividad 27
sentence=word.replace("because porque because", "")
print(sentence.strip())


#Actividad 28
print(empresa.startswith("codificacion"))


#Actividad 29
print(empresa.endswith("codificacion"))


#Actividad 30
espacios=" Codificacion para todos "
print(espacios.strip())


#Actividad 31
h1="30DaysOfPython"
h2="thirty_days_of_python"
print(h1.isidentifier())
print(h2.isidentifier())


#Actividad 32
librerias = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
unidos= "las siguientes son librarias:%s" % (librerias)
print(unidos) 


#Actividad 33
print("I am enjoying this challenge. \n I just wonder what is next.")


#Actividad 34
print("\tname     \tage    \tcountry")
print("\tcity")
print("\tAsabeneh \t250 \tFinland")
print("\tHelsinki")


#ACtividad 35
radius = 10
area = 3.14 * radius ** 2
print("el area del circulo con un radio de: %d es: %.2f" %(radius,area))


#Actividad 36
a=8
b=6
print("{} + {} = {}".format(a,b,a+b) )
print("{} - {} = {}".format(a,b,a-b) )
print("{} x {} = {}".format(a,b,a*b) )
print("{} / {} = {:.2f}".format(a,b,a/b) )
print("{} % {} = {}".format(a,b,a%b) )
print("{} // {} = {}".format(a,b,a//b))
print("{} ** {} = {}".format(a,b,a**b))
#final