"""
    Ejercicio # 1: Realice un programa en Python que dado como dato el sueldo de un trabajador, le aplique un aumento del 15% si su sueldo
    es inferior a $1000.00 y del 12% en caso contrario. Imprima el nuevo sueldo del trabajador.

    Nombre: SolucionEjercicio1.py
    Objetivo: Resolver ejercicio 1
    Autor: Lucio David Morán Brizuela
    Fecha: 26 de octubre de 2019
"""
def main():
    s = int(input("Ingrese su sueldo: "))
    if s<1000:
        s1 = s+s*0.15
        print("El nuevo sueldo del trabajador es: "+str(s1))
    else:
        s2 = s+s*0.12
        print("El nuevo sueldo del trabajador es: "+str(s2))
    
if __name__ == "__main__":
    main()