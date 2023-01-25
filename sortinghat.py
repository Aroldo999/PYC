Hufflepuff = 0
Slytherin = 0
Ravenclaw = 0
Gryffindor = 0


# pregunta 1

print ("Q1)Te gusta el amanecer o el atardecer?")

print("1 amanecer")
print("2 atardecer")

pregunta = int(input("respuesta (1-2):"))

if pregunta == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif pregunta == 2: 
    Hufflepuff += 1
    Slytherin += 1
else:
    print("input incorrecto")

# pregunta 2

print(" Q2)cuando muera, quiero que las personas me recuarden")

pregunta = int(input("respusta (1-4"))

print("El bueno")
print("El grande")
print("El sabio")
print("El audaz")

if pregunta == 1:
    Hufflepuff += 1
elif pregunta == 2:
    Slytherin += 1
elif pregunta == 3:
    Ravenclaw += 1
elif pregunta == 4:
    Gryffindor +=1
else:
    print("input incorrecto")

# pregnta 3

print("Q3)Cual de estos instrumentos prefieres escuchar")

pregunta = int(input("respusta (1-4"))

print("Violin")
print("Trompeta")
print("Piano")
print("Tambor")

if pregunta == 1:
    Slytherin += 1
elif pregunta == 2:
    Hufflepuff +=1
elif pregunta == 3:
    Ravenclaw += 1
elif pregunta == 4:
    Gryffindor += 1
else:
    print("input incorrecto")

# SIUUU

print(Hufflepuff)
print(Slytherin)
print(Ravenclaw)
print(Gryffindor)

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
    print("🦁 Gryffindor")
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
    print("🦅 Revenclaw")
elif Hufflepuff >= Slytherin:
    print("🦡 Hufflepuff")
else:
    print("🐍 Slytherin")
