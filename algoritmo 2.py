canasta = []
def ver_lista (lista):
    print("-------------------------------------------------------")
    for index, elemento in enumerate(lista):
        print(f"{index + 1}.- {elemento}")
    print("-------------------------------------------------------")
    
def agregar_elemento (lista):
    elemento = input("Que fruta quieres agregar?\n")
    lista.append(elemento)

def remover_elemento (lista):
    ver_lista(lista)
    print("Que desea eliminar?")
    r = int(input()) - 1
    lista.pop(r)
    

print("Bienvenido a abarrotes doña chencha")
agregar_elemento(canasta)

while True:
    r = input("que deseas hacer ahora?\n 1.- agregar otra fruta\n 2.- sacar fruta\n 3.- ver canasta\n 4.- salir\n")
    if r == "1":
        agregar_elemento(canasta)
    elif r == "2":
        remover_elemento(canasta)
    elif r == "3":
        ver_lista(canasta)
    elif r == "4":
        exit()
    else:
        "esta no es una opción válida"
