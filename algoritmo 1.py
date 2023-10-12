from random import random

print("--calculadora de esperanza de vida--")
print("Eres hombre o mujer?\n 1.-Hombre\n 2.-Mujer")
r = input()
suma = 0
if r == "1": suma += 76
else: suma += 78

r = input("fumas? (y/n)\n")
if r == "y": suma += -5
r = input("tomas alcohol? (y/n)\n")
if r == "y": suma += -5
r = input("consumes drogas? (y/n)\n")
if r == "y": suma += -15
print("Haces deporte?\n 1.- Diario\n 2.- Regularmente\n 3.- Nunca\n")
r = input()
if r == "1": suma += 5
elif r == "2": suma += 3

print("comes frutas y verduras?\n 1.- Si\n 2.- No\n 3.- solo frutas\n")
r = input()
if r == "1": suma += 5
elif r == "3": suma += 3
suerte = random() * 1000
if 20 < suerte < 40: suma += 20
else: suma += -20

print("regularmente cuánto duermes?\n 1.- Al menos 8hrs\n 2.- Al menos 6hrs\n 3.- Al menos 4hrs\n 4.- Al menos 2hrs\n 5.- 0hrs\n")
r = input()
if r == "1": suma += 5
elif r == "2": suma += 3
elif r == "3": suma += -4
elif r == "4": suma += -20
elif r == "5": suma += -50

print("Que tanto te enojas?\n 1.- Mucho 8hrs\n 2.- Poco\n 3.- nada\n")
r = input()
if r == "1": suma += -26
elif r == "2": suma += -2

print("que tan regularmente vas al médico?\n 1.- por lo menos 1 vez al año\n 2.- por lo menos 1 vez cada 10 años\n 3.- nunca\n")
r = input()
if r == "1": suma += 5
elif r == "2": suma += -5
elif r == "3": -15

print("Que raza eres?\n 1.- A\n 2.- B\n 3.- C\n 4.- D\n 5.- E\n")
r = input()
if r == "1": suma += 10
elif r == "2": suma += -2
elif r == "3": suma += 6
elif r == "4": suma += -1
elif r == "5": suma += 3

edad = int(input("cual es tu edad?\n"))
esperanza_vida = suma - edad

if esperanza_vida > 0: print(f"Te quedan {esperanza_vida} años de vida")
else: print("Podrías morir en cualquier momento ☠")