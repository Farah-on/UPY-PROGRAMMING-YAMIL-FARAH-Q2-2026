class DigitoVerificadorError(Exception):
    pass

check=True
while check:
    try:
        rol = input("Ingrese el rol: ")
        rol_sin_digito, digito = rol.split("-")
        check=False
    except ValueError:
        print("Rol incorrecto")

invertido = rol_sin_digito[::-1]

try:
    if not invertido.isnumeric():
        raise ValueError(f"{invertido} tiene caracteres no números")
except ValueError as e:
    print(e)

secuencia =[2,3,4,5,6,7]
suma=0

try:
    for index in range (len(invertido)):
        multiplicando=secuencia[index % 6]
        numero=int(invertido[index:index+1])
        suma+=numero * multiplicando
except ValueError:
    print("Escribe numeros")
except IndexError:
    print("Error de índice")-f