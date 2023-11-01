vocals = "aeiou"
word = input("introduce una palabra \n").lower()
for x in word:
    if x in vocals:
        tipo = "vocal"
    else:
        tipo = "consonante"
    print(x, "es una ", tipo)