import turnos

print("////BIENVENIDO A LA FARMACIA PYTHON////")
while True:
    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            departamento = input("Elija el departamento: ")
            ["P", "F", "C"].index(departamento)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break
    turnos.decorador(departamento)

    try:
        otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
        ["S", "N"].index(otro_turno)
    except ValueError:
        print("Esa noes una opción válida")
    else:
        if otro_turno == "N":
            print("Gracias por su visita")
            break

