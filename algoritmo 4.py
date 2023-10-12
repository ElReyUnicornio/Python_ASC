lista = ["Hola", "adios", "oso", "Hacha", "asa", "olvido", "aa", "e","Hola", "adios","Hola", "adios","asa","asa", "Hola", "Hola", "adios"]
print("Se encontraron estas palabras")
print("-----------------------------------------------")
for x in lista:
    if len(x) > 2 and x[0] == x[len(x) - 1]:
        print(x)
print("-----------------------------------------------")

print("palabras repetidas")
print("-----------------------------------------------")
repetidas = []
for x in lista:
    count = 0
    for y in lista:
        if x == y and (x not in repetidas):
            count += 1
    if count > 1:
        print(f"{x}\tx{count}")
        repetidas.append(x)
print("-----------------------------------------------")