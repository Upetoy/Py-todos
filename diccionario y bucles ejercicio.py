
paises={}

pais=input("Introduce el pais: ")

while pais!="salir":
    ciudad=input("Introduce Ciudad: ")

    lista_ciudades=paises.setdefault(pais,[ciudad])

    if lista_ciudades!=[ciudad]:
        paises[pais].append(ciudad)

    pais=input("Introduce el pais: ")

print(paises)




