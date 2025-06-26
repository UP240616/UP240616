#****Level 1****#
#Actividad 1 
tupla_vacia=tuple()


#Actividad 2
tupla_hermanas=("kimber","mariel")
tupla_hermanos=("ibrahim","israel")



#Actividad 3
hermanos=tupla_hermanos+tupla_hermanas


#Actividad 4
how_many=len(hermanos)
print("tengo:",how_many,"hermanos")


#Actividad 5
miembors_familia=list(hermanos)
miembors_familia.append("erika")
miembors_familia.append("neto")
print(miembors_familia)


#****LEVEL 2****#
#Actividad 1 
uno,dos,tres,cuatro,cinco,seis=miembors_familia


#Actividad 2
fruits=("naranja","platano","mango","guayaba")
vegetables=("apio","zanahoria","jitomate","lechuga")
animal_products=("leche","jamon","queso","yogurht")
food_stuf_tpl=fruits+vegetables+animal_products
print(food_stuf_tpl)


#Actvidad 3
food_stuf_it=list(food_stuf_tpl)


#Actividad 4
items_medios=food_stuf_it[0:6]
items_medio=food_stuf_it[7:12]
print(items_medios+items_medio)


#Actividad 5
tres=food_stuf_it[0:3]
last_tres=food_stuf_it[9:12]
print(tres)
print(last_tres)


#Actividad 6
del food_stuf_tpl


#Actividad 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("islandia" in nordic_countries)