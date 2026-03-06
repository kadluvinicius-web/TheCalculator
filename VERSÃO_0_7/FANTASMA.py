import random
import PRINCIPAL, ARQUIVOS

def Sorteio_Modos(número_min, número_máx):
    modos_escolhidos = ARQUIVOS.Ler_Arquivo('Modos Misto')
    modos_de_jogo = ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Exponenciação']
    modos_de_jogo_escolhidos = []
    for modo in range(5):
        if modos_escolhidos[modo] == 'True':
            modos_de_jogo_escolhidos.append(modos_de_jogo[modo])
    modo = random.choice(modos_de_jogo_escolhidos)
    número1 = 0
    número2 = 0
    sinal = ''

    if modo == 'Adição':
        número1 = random.randint(número_min, número_máx)
        número2 = random.randint(número_min, número_máx)
        sinal = '+'

    if modo == 'Subtração':
        número2 = random.randint(número_min, número_máx)
        número1 = random.randint(número2, número_máx)
        sinal = '-'

    if modo == 'Multiplicação':
        número1 = random.randint(número_min, número_máx)
        número2 = random.randint(número_min, número_máx)
        sinal = 'x'

    if modo == 'Divisão':
        while True:
            número2 = random.randint(número_min, número_máx)
            número1 = random.randint(número2, número_máx)
            divisão = str(número1 / número2)
            if len(divisão) == 3 and divisão[2] == '0':
                break
        sinal = '/'

    if modo == 'Exponenciação':
        número1 = random.randint(número_min, número_máx)
        número2 = random.randint(1, 3)
        sinal = '^'

    return número1, número2, sinal

def Fantasma():

    questões = ARQUIVOS.Ler_Arquivo('Quantidade')
    num_min = int(ARQUIVOS.Ler_Arquivo('Dificuldade')[0])
    num_máx = int(ARQUIVOS.Ler_Arquivo('Dificuldade')[1])
    lista_número1 = list()
    lista_número2 = list()
    lista_resultado = list()
    lista_sinais = list()
    questões_respondidas = 0
    questões_acertadas = 0
    questões_erradas = 0

    for pergunta in range(questões):

        valores = Sorteio_Modos(num_min, num_máx)
        número1 = valores[0]
        número2 = valores[1]
        sinal = valores[2]

        while True:
            try:
                resultado = str(input(f"Questão {pergunta+1}) {número1} ? {número2} = "))

                if resultado.upper() == 'S':
                    ARQUIVOS.Animação_Carregando('Saindo', 1)
                    print()
                    PRINCIPAL.Principal()
                else:
                    resultado = float(resultado)
                    break
            except ValueError:
                print(f"\033[91mDigite um número válido!\033[m")
            except KeyboardInterrupt:
                print()
                ARQUIVOS.Animação_Carregando('Saindo', 2)
                exit()

        lista_número1.append(número1)
        lista_número2.append(número2)
        lista_resultado.append(resultado)
        lista_sinais.append(sinal)

    ARQUIVOS.Animação_Carregando('Carregando', 2)
    print()
    for questão in range(questões):

        sinal = lista_sinais[questão]

        if sinal == '+':
            if lista_número1[questão] + lista_número2[questão] == lista_resultado[questão]:
                print(f"Questão {questão+1}) \033[92mResposta correta!\033[m")
                questões_acertadas += 1
            else:
                print(f"Questão {questão+1}) \033[91mResposta errada!\033[94m A resposta correta é {lista_número1[questão] + lista_número2[questão]}\033[m")
                questões_erradas += 1
            questões_respondidas += 1

        elif sinal == '-':
            if lista_número1[questão] - lista_número2[questão] == lista_resultado[questão]:
                print(f"Questão {questão + 1}) \033[92mResposta correta!\033[m")
                questões_acertadas += 1
            else:
                print(f"Questão {questão + 1}) \033[91mResposta errada!\033[94m A resposta correta é {lista_número1[questão] - lista_número2[questão]}\033[m")
                questões_erradas += 1
            questões_respondidas += 1

        elif sinal == 'x':
            if lista_número1[questão] * lista_número2[questão] == lista_resultado[questão]:
                print(f"Questão {questão+1}) \033[92mResposta correta!\033[m")
                questões_acertadas += 1
            else:
                print(f"Questão {questão+1}) \033[91mResposta errada!\033[94m A resposta correta é {lista_número1[questão] * lista_número2[questão]}\033[m")
                questões_erradas += 1
            questões_respondidas += 1

        elif sinal == '/':
            if lista_número1[questão] / lista_número2[questão] == lista_resultado[questão]:
                print(f"Questão {questão+1}) \033[92mResposta correta!\033[m")
                questões_acertadas += 1
            else:
                print(f"Questão {questão+1}) \033[91mResposta errada!\033[94m A resposta correta é {lista_número1[questão] / lista_número2[questão]}\033[m")
                questões_erradas += 1
            questões_respondidas += 1

        elif sinal == '^':
            if lista_número1[questão] ** lista_número2[questão] == lista_resultado[questão]:
                print(f"Questão {questão+1}) \033[92mResposta correta!\033[m")
                questões_acertadas += 1
            else:
                print(f"Questão {questão+1}) \033[91mResposta errada!\033[94m A resposta correta é {lista_número1[questão] ** lista_número2[questão]}\033[m")
                questões_erradas += 1
            questões_respondidas += 1

    ARQUIVOS.Adicionar_Arquivo(tipo='Estatísticas', conteúdo_questões_respondidas=questões_respondidas, conteúdo_questões_acertadas=questões_acertadas, conteúdo_questões_erradas=questões_erradas)
    PRINCIPAL.Principal()
