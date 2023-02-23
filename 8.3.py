meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

numeros = int(input("Dime un número del 1 al 12: "))


while numeros >12 or numeros <1:
  print("El mes no existe")
  numeros = int(input("Vuelve a probar: "))

  print(meses[numeros-1])

