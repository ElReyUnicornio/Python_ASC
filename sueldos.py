#en una empresa existen 3 puestos de nivel bajo
#operador, supervisor, jefe
#operador sueldo < 1000 -> bono = 15
#supervisor sueldo < 15000 -> bono = 20
#jefe sueldo > 2000 -> multa = 5
#salida sueldo de los trabajadores solicitados

no_trabajadores = int(input("Introduce el numero de trabajadores\n"))
mensaje = ""

for i in range(no_trabajadores):
    puesto = input(f"introduce el puesto del trabajador No. {i +1}\n")
    sueldo = int(input(f"introduce el sueldo del trabajador No. {i +1}\n"))
    mensaje += "------------------------------------------\n"
    mensaje += f"Trabajador No.{i+1}\n"
    mensaje += f"Sueldo: {sueldo}\n"
    
    if (puesto == "operador" and sueldo < 1000):
        bono = 15 * sueldo / 100
        mensaje += f"Bono: {bono}\n"
        
    if (puesto == "supervisor" and sueldo < 5000):
        bono = 20 * sueldo / 100
        mensaje += f"Bono: {bono}\n"
    
    if (puesto == "dueño"    ):
        bono = 10000
        mensaje += f"Bono: {bono}\n"
        
    if (puesto == "jefe" and sueldo > 20000):
        bono = 15 * sueldo / 100 * -1
        mensaje += f"Multa: {bono}\n"
        
    mensaje += f"Total: {sueldo + bono}\n"

print(mensaje)