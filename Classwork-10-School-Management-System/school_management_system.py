#Input
usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno',    'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno',    'nombre': 'Ana Martín'},
    'cgarcia': {'password': '1234', 'rol': 'alumno', 'nombre': 'Carlos García'},
    'lmendez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Laura Méndez'},
    'rlopez':  {'password': '1234', 'rol': 'alumno', 'nombre': 'Roberto López'},
    'msantos': {'password': '1234', 'rol': 'alumno', 'nombre': 'María Santos'},
# one teacher who teaches all subjects, one coordinator,
    'mlopez': {'password': '1234', 'rol': 'maestro',    'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador',    'nombre': 'Rosa García'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')
calificaciones = {
    'jperez':  {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 6.0},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'cgarcia': {'Matemáticas': 8.0, 'Programación': 8.5, 'Inglés': 7.5},
    'lmendez': {'Matemáticas': 8.5, 'Programación': 6.0, 'Inglés': 8.0},
    'rlopez':  {'Matemáticas': 7.5, 'Programación': 8.0, 'Inglés': 8.5},
    'msantos': {'Matemáticas': 3.0, 'Programación': 8.5, 'Inglés': 8.0}
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
    print("\n" + "-" * 60)
    print(f"{'Alumno':20}|{'Matemáticas':12}|{'Programación':12}|{'Inglés':8}")
    print("-" * 60)
    
    for alumno, notas in calificaciones.items():
        print(
            f"{usuarios[alumno]['nombre']:20}|"
            f"{notas['Matemáticas']:12}|"
            f"{notas['Programación']:12}|"
            f"{notas['Inglés']:8}"
            )
        print("-" * 60)