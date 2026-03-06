import NOVIDADES, TELAS, ARQUIVOS

def Principal():
    opção_jogador = TELAS.Tela_Principal()

    if opção_jogador == 1:
        TELAS.Tela_Modos_Jogo()

    elif opção_jogador == 2:
        TELAS.Tela_Configurações()

    elif opção_jogador == 3:
        TELAS.Tela_Estatísticas()

    elif opção_jogador == 4:
        conta_logada = ARQUIVOS.Ler_Arquivo('Conta_Logada')
        if not conta_logada or conta_logada[0] == 'None' and conta_logada[1] == 'None':
            TELAS.Tela_Sem_Conta()
        else:
            TELAS.Tela_Com_Conta(conta_logada[0], conta_logada[1])

    elif opção_jogador == 5:
        ARQUIVOS.Animação_Carregando('Carregando', 2)
        print()
        NOVIDADES.Novidades()

    elif opção_jogador == 6:
        ARQUIVOS.Animação_Carregando('Saindo', 2)
        exit()

if __name__ == "__main__":
    Principal()
