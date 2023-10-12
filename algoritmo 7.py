def matrizPrint(lista):
    print("\n")
    mensaje= "\n   "
    for i in range(len(lista[0])):
        mensaje += f" {i + 1} "
    mensaje += "\n"
    print(mensaje)
    for i,y in enumerate(lista):
        print(f"{i + 1}  {lista[i]}")
    
    

def generar_lista(bounds):
    lista = []
    for i in range(x):
        lista.append([])
        for j in range(x):
            lista[i].append(0)
    return lista

def vertical(col, list):
    for el in list:
        for i in range(col - 1,len(list) - col):
            el[col - 1 + i] = 1
    matrizPrint(list)
    
def horizontal(fila, list):
    for i,el in enumerate(list[fila-1]):
        list[fila - 1][i] = 1
    matrizPrint(list)
    
#def diagonal():
    

x = int(input("Cuacuanto quieres que mida tu matriz?\n"))
lista = generar_lista(x)

matrizPrint(lista)
vertical(3, lista)
horizontal(3, lista)

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