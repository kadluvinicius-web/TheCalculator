import PRINCIPAL, ARQUIVOS

def Dobro_Em_Dobro():

    número1 = 1
    pergunta = 1
    dificuldade = 92
    acertos = True

    while acertos:

        while True:
            try:
                resultado = str(input(f"Questão {pergunta}) \033[{dificuldade}m{número1} * {2} = \033[m"))
                if resultado.upper() == 'S':
                    ARQUIVOS.Animação_Carregando('Saindo', 1)
                    print()
                    PRINCIPAL.Principal()
                else:
                    resultado = int(resultado)
                    break
            except ValueError:
                print(f"Digite um número válido!")
            except KeyboardInterrupt:
                print()
                ARQUIVOS.Animação_Carregando('Saindo', 2)
                exit()

        if resultado == número1 * 2:
            número1 *= 2
            pergunta += 1
            if pergunta > 10:
                dificuldade = 93
            if pergunta > 25:
                dificuldade = 91

        else:
            print("\033[91mErrou! Tente novamente.\033[m")
            acertos = False


    PRINCIPAL.Principal()

def Fibonacci():
    número1 = 0
    número2 = 1
    pergunta = 1
    dificuldade = 92
    acertos = True

    while acertos:

        while True:
            try:
                resultado = str(input(f"Questão {pergunta}) \033[{dificuldade}m{número1} + {número2} = \033[m"))
                if resultado.upper() == 'S':
                    ARQUIVOS.Animação_Carregando('Saindo', 1)
                    print()
                    PRINCIPAL.Principal()
                else:
                    resultado = int(resultado)
                    break
            except ValueError:
                print(f"Digite um número válido!")
            except KeyboardInterrupt:
                print()
                ARQUIVOS.Animação_Carregando('Saindo', 2)
                exit()

        if resultado == número1 + número2:
            número1 = número2
            número2 = resultado
            pergunta += 1
            if pergunta > 10:
                dificuldade = 93
            if pergunta > 25:
                dificuldade = 91

        else:
            print("\033[91mErrou! Tente novamente.\033[m")
            acertos = False

    PRINCIPAL.Principal()
