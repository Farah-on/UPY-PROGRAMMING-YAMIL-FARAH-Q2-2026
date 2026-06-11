#Digito verificador

#Obtener el numero sin digito verificador
rol = input("Ingrese el rol sin digito verificador: ")


#Invertir el numero 
rol_invertido = rol[::-1]

#Multiplicar los digitos por la secuencia
multiplicadores = [2, 3, 4, 5, 6, 7]
suma = 0

for i in range(len(rol_invertido)):
    digito = int(rol_invertido[i])
    multiplicador = multiplicadores[i % len(multiplicadores)]
    suma += digito * multiplicador
    
# Calcular el modulo 11
resto = suma % 11