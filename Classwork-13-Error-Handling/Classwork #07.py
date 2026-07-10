class DigitoVerificadorError(Exception):
    pass

rol = input("Ingrese el rol: ")
try:
    rol_sin_digito, digito = rol.split("-")
except ValueError:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")
    rol_sin_digito, digito = None, None

if rol_sin_digito is not None:
    try:
        if not rol_sin_digito.isnumeric():
            raise ValueError("Los digitos del rol deben ser numéricos")
        if not digito.isnumeric():
            raise ValueError("El digito verificador debe ser numérico")
    except ValueError as e:
        print(e)
        rol_sin_digito = None

if rol_sin_digito is not None:
    invertido = rol_sin_digito[::-1]
    secuencia =[2,3,4,5,6,7]
    suma=0
    try:
        for index in range (len(invertido)):
            multiplicando=secuencia[index % 6]
            numero=int(invertido[index:index+1])
            suma+=numero * multiplicando
    except ValueError:
        print("Escribe numeros")
        rol_sin_digito = None
    except IndexError:
        print("Error de índice")
        rol_sin_digito = None

if rol_sin_digito is not None:
    # Calcular el modulo 11
    resto = suma % 11
    #Restar el resultado a 11
    dv = 11 - resto
    #Mostrar el dígito verificador
    try:
        if str(dv) != digito:
            raise DigitoVerificadorError(f"Error: El dígito verificador no conicide, se esperaba {dv}")
    except DigitoVerificadorError as p:
        print(p)
    else:
        print(rol)