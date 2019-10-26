"""
    Ejercicio # 2: Realice un programa en Python que dado como datos la categoría y el sueldo de un trabajor, calcule el aumento 
    correspondiente teniendo en cuenta la siguiente información e imprima el nuevo sueldo del trabajador:
        <li>Categoría 1 : Aumento 15%</li>
        <li>Categoría 2 : Aumento 10%</li>
        <li>Categoría 3 : Aumento 8%</li>
        <li>Categoría 4 : Aumento 7%</li>

    Nombre: SolucionEjercicio2.py
    Objetivo: Resolver ejercicio 2
    Autor: Lucio David Morán Brizuela
    Fecha: 26 de octubre de 2019
"""
def main():
    s = int(input("Ingrese su sueldo: "))
    c = int(input("Ingrese su categoría [Entre 1-4]: "))
    if int(c) == 1:
        s1 = s+s*0.15
        print("El nuevo sueldo del trabajador es: "+str(s1))
    elif int(c) == 2:
        s2 = s+s*0.10
        print("El nuevo sueldo del trabajador es: "+str(s2))
    elif int(c) == 3:
        s3 = s+s*0.08
        print("El nuevo sueldo del trabajador es: "+str(s3))
    elif int(c) == 4:
        s4 = s+s*0.07
        print("El nuevo sueldo del trabajador es: "+str(s4))
    else:
        print("ERROR: Ingrese una categoría válida entre 1 y 4")
    
if __name__ == "__main__":
    main()