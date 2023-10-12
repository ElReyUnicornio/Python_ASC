def sumar_lista (lista):
    return sum(x for x in lista)

def multiplicar_lista(lista):
    multiplicacion = 1
    for x in lista:
        multiplicacion *= x
    return multiplicacion

def mayor (lista):
    for x in lista:
        for index,y in enumerate(lista):
            old = 0
            new = 0
            if index + 1 == len(lista): continue;
            if y < lista[index + 1]:
                new = lista[index + 1]
                old = y
                lista[index] = new
                lista[index + 1] = old
    return lista[0]

def menor (lista):
    for x in lista:
        for index,y in enumerate(lista):
            old = 0
            new = 0
            if index + 1 == len(lista): continue;
            if y > lista[index + 1]:
                new = lista[index + 1]
                old = y
                lista[index] = new
                lista[index + 1] = old
    return lista[0]
            

list = [10,3,4]

print(sumar_lista(list))
print(multiplicar_lista(list))
print(mayor(list))
print(menor(list))
