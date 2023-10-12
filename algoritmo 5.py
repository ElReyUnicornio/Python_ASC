def diagonal (lista):
    sum=0
    for i, x in enumerate(lista):
        sum += x[i]
    return sum

def diagonal_i (lista):
    sum=0
    for i, x in enumerate(lista):
        sum += x[len(x) -i -1]
    return sum

lista = [
    [1,2,20],
    [4,5,6],
    [7,8,10]
]

print(f"diagonal normal: {diagonal(lista)}")
print(f"diagonal inversa: {diagonal_i(lista)}")