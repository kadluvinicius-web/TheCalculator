import sys, time

def Adicionar_Arquivo(tipo, conteúdo_quantidade=10, conteúdo_dificuldade_mínimo=0, conteúdo_dificuldade_máximo=10, conteúdo_decimais=0, nome='', senha='', conteúdo_questões_respondidas=0, conteúdo_questões_acertadas=0, conteúdo_questões_erradas=0, adição=True, subtração=True, multiplicação=True, divisão=True, exponenciação=True, radiciação=True):

    if tipo == 'Quantidade':
        file = open('QUANTIDADE_DE_QUESTÕES.txt', 'at')
        conta = Ler_Arquivo(tipo='Número_Conta')
        texto = f'\n({conta}) {conteúdo_quantidade}'
        file.write(texto)

    elif tipo == 'Dificuldade':
        file = open('NÚMERO_MÍNIMO_E_MÁXIMO.txt', 'at')
        conta = Ler_Arquivo(tipo='Número_Conta')
        texto = f'\n({conta}) {conteúdo_dificuldade_mínimo} | {conteúdo_dificuldade_máximo}'
        file.write(texto)

    elif tipo == 'Decimais':
        file = open('CASAS_DECIMAIS_DIVISÃO.txt', 'at')
        conta = Ler_Arquivo(tipo='Número_Conta')
        texto = f'\n({conta}) {conteúdo_decimais}'
        file.write(texto)

    elif tipo == 'Conta':
        file = open('CONTAS.txt', 'at')
        texto = f'{nome} | {senha}\n'
        file.write(texto)

    elif tipo == 'Conta_Logada':
        file = open('CONTA_LOGADA.txt', 'at')
        texto = f'\n{nome} | {senha}'
        file.write(texto)

    elif tipo == 'Estatísticas':
        file = open('ESTATÍSTICAS.txt', 'at')
        conta = Ler_Arquivo(tipo='Número_Conta')
        estatísticas = Ler_Arquivo(tipo='Estatísticas')
        texto = f'\n({conta}) {int(estatísticas[0])+conteúdo_questões_respondidas} | {int(estatísticas[1])+conteúdo_questões_acertadas} | {int(estatísticas[2])+conteúdo_questões_erradas}'
        file.write(texto)

    elif tipo == 'Modos Misto':
        file = open('MODOS_MISTO.txt', 'at')
        conta = Ler_Arquivo(tipo='Número_Conta')
        texto = f'\n({conta}) {adição} | {subtração} | {multiplicação} | {divisão} | {exponenciação} | {radiciação}'
        file.write(texto)

def Ler_Arquivo(tipo):

    if tipo == 'Quantidade':
        file = open('QUANTIDADE_DE_QUESTÕES.txt', 'rt')
        conta = Ler_Arquivo(tipo='Número_Conta')
        linhas = list()
        for linha in file:
            if f'({conta})' in linha:
                linha = linha.replace(f'({conta}) ', '')
                linhas.append(linha)

        try:
            return int(linhas[-1])
        except IndexError:
            return 10

    elif tipo == 'Dificuldade':
        file = open('NÚMERO_MÍNIMO_E_MÁXIMO.txt', 'rt')
        conta = Ler_Arquivo(tipo='Número_Conta')
        linhas = list()
        for linha in file:
            if f'({conta})' in linha:
                linha = linha.replace(f'({conta}) ', '')
                linhas.append(linha)

        try:
            linhas[-1] = linhas[-1].split(' | ')
            return linhas[-1]
        except IndexError:
            return 1, 10

    elif tipo == 'Decimais':
        file = open('CASAS_DECIMAIS_DIVISÃO.txt', 'rt')
        conta = Ler_Arquivo(tipo='Número_Conta')
        linhas = list()
        for linha in file:
            if f'({conta})' in linha:
                linha = linha.replace(f'({conta}) ', '')
                linhas.append(linha)

        try:
            return int(linhas[-1])
        except IndexError:
            return 0

    elif tipo == 'Estatísticas':
        file = open('ESTATÍSTICAS.txt', 'rt')
        conta = Ler_Arquivo(tipo='Número_Conta')
        linhas = list()
        for linha in file:
            if f'({conta})' in linha:
                linha = linha.replace(f'({conta}) ', '').replace('\n', '')
                linhas.append(linha)

        try:
            linhas[-1] = linhas[-1].split(' | ')
            return linhas[-1]
        except IndexError:
            return 0, 0, 0

    elif tipo == 'Modos Misto':
        file = open('MODOS_MISTO.txt', 'rt')
        conta = Ler_Arquivo(tipo='Número_Conta')
        linhas = list()
        for linha in file:
            if f'({conta})' in linha:
                linha = linha.replace(f'({conta}) ', '').replace('\n', '')
                linhas.append(linha)

        try:
            linhas[-1] = linhas[-1].split(' | ')
            return linhas[-1]
        except IndexError:
            return 'True', 'True', 'True', 'True', 'True', 'True'

    elif tipo == 'Conta_Logada':
        file = open('CONTA_LOGADA.txt', 'rt')
        linhas = list()
        for linha in file:
            linhas.append(linha)

        try:
            linhas[-1] = linhas[-1].split(' | ')
            return linhas[-1]
        except IndexError:
            return False

    elif tipo == 'Número_Conta':
        file = open('CONTAS.txt', 'rt')
        num_conta = 0
        conta_logada = Ler_Arquivo(tipo='Conta_Logada')
        for linha in file:
            linha = linha.replace('\n', '').split(' | ')
            num_conta += 1
            if linha == conta_logada:
                return num_conta

    elif 'Conta' in tipo:
        file = open('CONTAS.txt', 'rt')
        nomes = list()
        senhas = list()
        for linha in file:
            linha = linha.replace('\n', '')
            linha = linha.split(' | ')
            nomes.append(linha[0])
            senhas.append(linha)

        try:
            if tipo == 'Conta_Nome':
                return nomes
            elif tipo == 'Conta_Senha':
                return senhas
        except IndexError:
            print("corrigir IndexError!")

def Animação_Carregando(texto, vezes, modo=''):
    c = 0

    for i in range(0, vezes * 4):
        sys.stdout.write(f'\r{texto}{c}'.replace(f'{c}', '.' * c))
        c += 1

        if c > 3:
            c = 0

        sys.stdout.flush()
        time.sleep(0.3)

    if modo == 'Carregar':
        print()
