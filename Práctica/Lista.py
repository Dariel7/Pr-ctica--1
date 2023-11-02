ciudades =[]

for i in range(5):
    ciudad = input("Ingrese el nombre de una ciudad: ")
    ciudades.append(ciudad)

print("Las ciudades ingresadas son:")
for ciudad in ciudades:
    print(ciudad)