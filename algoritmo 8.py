def Menu():
    print("-----------------------------------------------------------------------")
    Mostrar_lista(productos)
    print("\n",len(productos) + 1, ".- Pagar")
    print(len(productos) + 2, ".- Salir")
    print("-----------------------------------------------------------------------")

def Mostrar_lista(lista):
    for i,x in enumerate(lista):
        print(f"{i + 1}.- " + str(x["nombre"]))
        
def agregar(producto):
    cant = int(input("Indique la cantidad que deseé agregar:\n"))
    for x in carrito:
        if x["nombre"] == producto["nombre"]:
            x["cantidad"] += cant
            break

carrito = []

productos = [
    {
        "nombre": "Papas",
        "precio": 57
    },
    {
        "nombre": "Sabritas",
        "precio": 20
    },
    {
        "nombre": "Coca-Cola",
        "precio": 17
    },
    {
        "nombre": "Sopa",
        "precio": 10
    },
    {
        "nombre": "Aguacate",
        "precio": 80
    },
]

print("Bienvenido a nuestra tienda")
Menu()
r = int(input("Que desea hacer ahora?\n"))
