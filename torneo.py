#en un torneo de apertura de futbol se desea calcular el puntaje de los equipos
#por cada partido ganado se va a aumentar 3 puntos
#por un partido empatado se suma 1 punto
#por un partido perdido se obtienen 0 puntos

#No. partidos jugados
#segun los num jugados pedir el resultado

#calcular p/c/pjugado

#salida total de puntos
n_partidos = int(input("Introduce el numero de partidos jugados\n"))

puntuacion_eq1 = 0
puntuacion_eq2 = 0
mensaje = ""
for i in range(n_partidos):
    res = input(f"cual fue el resultado del partido {i + 1}? (ganado / perdido / empatado)\n").lower()
    print(res)
    if (res == "ganado"):
        puntuacion_eq1 += 3
        mensaje += ("3\t\t0\n")
    if (res == "perdido"):
        puntuacion_eq2 += 3
        mensaje += ("0\t\t3\n")
    if (res == "empatado"):
        puntuacion_eq1 += 1
        puntuacion_eq2 += 1
        mensaje += ("1\t\t1\n")

print("Equipo 1\tEquipo 2")
print("----------------------------------------------------------------")
print(mensaje)
print("----------------------------------------------------------------")
print("total")
print("----------------------------------------------------------------")
print(puntuacion_eq1,"\t\t", puntuacion_eq2)