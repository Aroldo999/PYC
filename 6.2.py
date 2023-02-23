
clave = input("Introduzca tu clave de usuario")
contraseña = input("Introduzca tu contraseña de usuario")


while clave != ("admin") or contraseña != "0987":
    print("INCORRECTO, vuelve a intentarlo:")
    clave = input("Introduzca tu clave de usuario:")
    contraseña = input("Introduzca tu contraseña de usuario:")


print("CORRECTO, que tenga un buen día")