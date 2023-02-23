num = []

for i in range (0,10):
   num.append(int(input("Dame un numeros")))

print("Los pares de estos numeros son")
for i in range (0,10):
   if num[i] % 2 == 0:
      print(num[i])
