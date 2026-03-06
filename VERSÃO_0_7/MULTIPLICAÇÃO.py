import random
import PRINCIPAL, ARQUIVOS

def Multiplicação():

    questões = ARQUIVOS.Ler_Arquivo('Quantidade')
    num_min = int(ARQUIVOS.Ler_Arquivo('Dificuldade')[0])
    num_máx = int(ARQUIVOS.Ler_Arquivo('Dificuldade')[1])
    lista_número1 = list()
    lista_número2 = list()
    lista_resultado = list()
    questões_respondidas = 0
    questões_acertadas = 0
    questões_erradas = 0

    for pergunta in range(questões):

        número1 = random.randint(num_min, num_máx)
        número2 = random.randint(num_min, num_máx)

        while True:
            try:
                resultado = str(input(f"Questão {pergunta + 1}) {número1} * {número2} = "))
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

        lista_número1.append(número1)
        lista_número2.append(número2)
        lista_resultado.append(resultado)

    ARQUIVOS.Animação_Carregando('Carregando', 2)
    print()
    for questão in range(questões):
        if lista_número1[questão] * lista_número2[questão] == lista_resultado[questão]:
            print(f"Questão {questão+1}) \033[92mResposta correta!\033[m")
            questões_acertadas += 1
        else:
            print(f"Questão {questão+1}) \033[91mResposta errada!\033[94m A resposta correta é {lista_número1[questão] * lista_número2[questão]}\033[m")
            questões_erradas += 1
        questões_respondidas += 1

    ARQUIVOS.Adicionar_Arquivo(tipo='Estatísticas', conteúdo_questões_respondidas=questões_respondidas, conteúdo_questões_acertadas=questões_acertadas, conteúdo_questões_erradas=questões_erradas)
    PRINCIPAL.Principal()
