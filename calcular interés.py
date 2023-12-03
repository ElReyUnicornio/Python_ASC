# calcular interés
# entradas {capital, % interés, plazo años}
# salidas {Total de capital}

capital = int(input("introduce el capital inicial"))
interes = int(input("introduce la tasa de interés"))
plazo = int(input("introduce el plazo a pagar en años"))
total = 0

total += capital
for i in range(plazo):
    total += (total * (interes/100))

print("Total: ", total)
