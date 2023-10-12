def matrizPrint(lista):
    print("\n")
    mensaje= "\n   "
    for i,y in enumerate(lista):
        print(f"{len(lista) - i}  {lista[i]}")
    for i in range(len(lista[0])):
        mensaje += f" {i + 1} "
    mensaje += "\n"
    print(mensaje)
    

def generar_lista(x, y):
    lista = []
    for i in range(y):
        lista.append([])
        for j in range(x):
            lista[i].append(0)
    return lista

x = int(input("Cual quieres que sea el largo de tu matriz?\n"))
y = int(input("Cual quieres que sea el alto de tu matriz?\n"))

lista = generar_lista(x, y)
matrizPrint(lista)
while True:
    r = input("desea cambiar algún espacio? (s/n)")
    if r == "s":
        r = input("ingresa el espacio que deseas cambiar (utiliza el formato x,y sin espacios)\n")
        coordenadas = r.split(",")
        x = len(lista) - int(coordenadas[1])
        y = int(coordenadas[0]) - 1
        print(x,y)
        lista[x][y] = 1
        matrizPrint(lista)
    else:
        exit()