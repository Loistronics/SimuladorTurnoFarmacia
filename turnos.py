def turnoPerfumeria():
    for i in range(1,10000):
        yield f"P - {i}"

def turnoFarmacia():
    for i in range(1,10000):
        yield f"F - {i}"

def turnoCosmetico():
    for i in range(1,10000):
        yield f"C - {i}"

p = turnoPerfumeria()
f = turnoFarmacia()
c = turnoCosmetico()


def decorador(departamento):
    print("\n" + "*" * 23)
    print("Su número es:")
    if departamento == "P":
        print(next(p))
    elif departamento == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print("*" * 23 + "\n")
