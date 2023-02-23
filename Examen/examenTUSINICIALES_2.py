#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba el día correspondiente.
#Si introducimos otro número nos da un error y nos vuelve a solicitar el número de día.
#  (Haz dos versiones: una sin utilizar listas (examenTUSINICIALES_1.py) y otra con listas (examenTUSINICIALES_2.py)

  

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

while True:
  try:
      numero_dia = int(input("Ingrese un número del 1 al 7 para representar un día de la semana: "))
      if 1 <= numero_dia <= 7:
          print("El día correspondiente es", dias[numero_dia - 1])
          break
      else:
          print("El número debe estar entre 1 y 7. Intente nuevamente.")
  except ValueError:
        print("El valor ingresado no es un número. Intente nuevamente.")
