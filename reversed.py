def reverse(lista):
    res = ""
    for i in range(len(lista) - 1, -1, -1):
        res += lista[i]
    return res

message = input("Introduce un texto\n")
print(reverse(message))