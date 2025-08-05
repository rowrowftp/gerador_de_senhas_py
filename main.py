from random import randint

def gera_senha():
    tam = int(input("Digite o tamanho da senha (em números)\n> "))
    initial = input("\nDigite os caracteres na senha (deixe vazio para preenchimento automático)\n> ")
    auto = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%¨&*()-_=+[]{}<>,.;:´`\/'"

    chars = "_" * tam
    charlist = chars.split("_")
    tamanho = len(initial)-1

    if initial == "":
        tamanho = len(auto)-1
        for i in range(tam+1):
            charlist[i] = auto[randint(0, tamanho)]
    else:
        for i in range(tam+1):
            charlist[i] = initial[randint(0, tamanho)]

    for i in range(tam+1):
        decisor = randint(0, 1)
        if decisor == 1:
            try:
                charlist[i] = charlist[i].upper()
            except:
                pass
        else:
            pass

    senha = "".join(charlist)
    print(f'\nSua senha é: {senha}')

while True:
    try:
        gera_senha()
        break
    except ValueError:
        print("\nDigite um tamanho em digitos!\n")
