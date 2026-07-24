#Input
usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno',    'nombre': 'Juan Pérez'},
    'dromo': {'password': '1234', 'rol': 'alumno',    'nombre': 'Daniela Romo'},
    'mjuarez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Mauricio Juárez'},
    'mlopez': {'password': '1234', 'rol': 'alumno', 'nombre': 'María López'},
    'euc':  {'password': '1234', 'rol': 'alumno', 'nombre': 'Ernesto Uc'},
    'cbalam': {'password': '1234', 'rol': 'alumno', 'nombre': 'Carlos Balam'},
# one teacher who teaches all subjects, one coordinator,
    'jpedrozo': {'password': '1234', 'rol': 'maestro',    'nombre': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'rol': 'coordinador',    'nombre': 'Didier Gamboa'}
}

materias = ('Matemáticas Discretas', 'Programación', 'Inglés II', 'Cálculo Diferencial', 'Probabilidad y Estadística', 'Arquitectura de Computadoras y Servidores', 'Habilidades Socioemocionales y Manejo de Conflictos')
calificaciones = {
    'jperez':  {'Matemáticas Discretas': 8.5, 'Programación': 9.2, 'Inglés II': 9.0, 'Cálculo Diferencial': 7.8, 'Probabilidad y Estadística': 8.3, 'Arquitectura de Computadoras y Servidores': 6.8, 'Habilidades Socioemocionales y Manejo de Conflictos': 9.5},
    'dromo': {'Matemáticas Discretas': 9.0, 'Programación': 6.7, 'Inglés II': 9.4, 'Cálculo Diferencial': 6.2, 'Probabilidad y Estadística': 9.1, 'Arquitectura de Computadoras y Servidores': 6.5, 'Habilidades Socioemocionales y Manejo de Conflictos': 9.8},
    'mjuarez': {'Matemáticas Discretas': 7.5, 'Programación': 8.0, 'Inglés II': 8.5, 'Cálculo Diferencial': 7.0, 'Probabilidad y Estadística': 7.8, 'Arquitectura de Computadoras y Servidores': 6.2, 'Habilidades Socioemocionales y Manejo de Conflictos': 8.9},
    'mlopez': {'Matemáticas Discretas': 9.5, 'Programación': 9.8, 'Inglés II': 9.2, 'Cálculo Diferencial': 9.0, 'Probabilidad y Estadística': 9.6, 'Arquitectura de Computadoras y Servidores': 9.4, 'Habilidades Socioemocionales y Manejo de Conflictos': 10.0},
    'euc':  {'Matemáticas Discretas': 8.2, 'Programación': 6.9, 'Inglés II': 8.8, 'Cálculo Diferencial': 6.0, 'Probabilidad y Estadística': 6.4, 'Arquitectura de Computadoras y Servidores': 8.1, 'Habilidades Socioemocionales y Manejo de Conflictos': 9.0},
    'cbalam': {'Matemáticas Discretas': 8.8, 'Programación': 9.0, 'Inglés II': 8.5, 'Cálculo Diferencial': 6.6, 'Probabilidad y Estadística': 8.9, 'Arquitectura de Computadoras y Servidores': 8.7, 'Habilidades Socioemocionales y Manejo de Conflictos': 9.2}
}

#Process
while True:
    apodo = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if apodo in usuarios and contraseña == usuarios[apodo]["password"]:
        print("Bienvenido", usuarios[apodo]["nombre"])
        break
    else:
        print("Usuario incorrecto o contraseña incorrecta")
rol = usuarios[apodo]["rol"]
if rol == "alumno":
    aprobadas = set()
    print("Boleta de", usuarios[apodo]["nombre"])
    for materia in materias:
        print(materia, calificaciones[apodo][materia])
        if calificaciones[apodo][materia] >= 7:
            aprobadas.add(materia)

    pendientes = set(materias) - aprobadas
    print("Aprobadas:", aprobadas)
    print("Pendientes:", pendientes)


elif rol == "maestro":
    print("Rol:", usuarios[apodo]["rol"])
    print("Alumnos:")
    for usuario in calificaciones:
        print("-", usuarios[usuario]["nombre"])
        print()
    print("\nMaterias:")
    for materia in materias:
        print("-", materia)
    cambio = input("¿Quieres cambiar la calificación de un alumno? (si/no)")
    while cambio == "si":
        alumno = input("Alumno: ")
        materia = input("Materia: ")
        if alumno in calificaciones and materia in materias:
            nueva = float(input("Nueva calificación: "))
            seguridad = input("¿Estás seguro(si/no):  ")
            if seguridad == "si":
                calificaciones[alumno][materia] = nueva
                print("Calificaciones actualizadas de", usuarios[alumno]["nombre"])
                for materia in materias:
                    print(materia, calificaciones[alumno][materia])
        else:
            print("alumno no encontrado")
        cambio = input("¿Quieres cambiar otra calificación? (si/no)")

elif rol == "coordinador":

    print("Maestros:")
    for usuario, datos in usuarios.items():
        if datos["rol"] == "maestro":
            print(datos["nombre"])
    print()
    ancho_nombre = 20
    ancho_col = 12
    ancho_total = ancho_nombre + ancho_col * len(materias) + len(materias)
    print("\n" + "-" * ancho_total)
    encabezado = f"{'Alumno':{ancho_nombre}}" + "".join(f"|{materia:{ancho_col}}" for materia in materias)
    print(encabezado)
    print("-" * ancho_total)

    for alumno, notas in calificaciones.items():
        fila = f"{usuarios[alumno]['nombre']:{ancho_nombre}}" + "".join(f"|{notas[materia]:{ancho_col}}" for materia in materias)
        print(fila)
        print("-" * ancho_total)