#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba el día correspondiente.
#Si introducimos otro número nos da un error y nos vuelve a solicitar el número de día.
#  (Haz dos versiones: una sin utilizar listas (examenTUSINICIALES_1.py) y otra con listas (examenTUSINICIALES_2.py)



numero = int(input("Dime que de de la semana es hoy según el número del 1 al 7:"))

if numero == 1:
    print("Es Lunes")
elif numero == 2:
    print("Es Martes")
elif numero == 3:
    print("Es Mircoles")
elif numero == 4:
    print("Es Jueves")
elif numero == 5:
    print("Es Viernes")
elif numero == 6:
    print("Es Sabado")
elif numero == 7:
    print("Es Domingo")
while numero <0 or numero >8 :
    int(input("Error, intentelo otra vez: "))

