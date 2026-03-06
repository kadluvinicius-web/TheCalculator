import PRINCIPAL, ARQUIVOS, ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO, EXPONENCIAÇÃO, RADICIAÇÃO, MISTO, FANTASMA, MINI_GAMES


def Tela_Principal():
    tela = ("----------------The-Calculator----------------\n"
            "(1) Jogar             | (4) Conta\n"
            "(2) Configurações     | (5) Novidades\n"
            "(3) Estatísticas      | (6) Sair")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 6:
                break
            else:
                print("\033[91mDigite um número entre 1 e 6!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    return opção_escolhida

def Tela_Modos_Jogo():
    tela = ("----------------The-Calculator----------------\n"
            "(1) Modos Clássicos\n"
            "(2) Modos Especiais\n"
            "(3) Voltar")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 3:
                break
            else:
                print("\033[91mDigite um número entre 1 e 3!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        Tela_Modos_Clássicos()
    if opção_escolhida == 2:
        Tela_Modos_Especiais()
    if opção_escolhida == 3:
        PRINCIPAL.Principal()

def Tela_Modos_Clássicos():
    tela = ("----------------The-Calculator----------------\n"
            "\033[93m(1) Adição\033[m            | \033[96m(5) Exponenciação\n"
            "\033[94m(2) Subtração\033[m         | \033[90m(6) Radiciação\n"
            "\033[92m(3) Multiplicação\033[m     | (7) Voltar\n"
            "\033[91m(4) Divisão\033[m           |")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 7:
                break
            else:
                print("\033[91mDigite um número entre 1 e 7!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        ADIÇÃO.Adição()

    elif opção_escolhida == 2:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        SUBTRAÇÃO.Subtração()

    elif opção_escolhida == 3:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        MULTIPLICAÇÃO.Multiplicação()

    elif opção_escolhida == 4:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        DIVISÃO.Divisão()

    elif opção_escolhida == 5:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        EXPONENCIAÇÃO.Exponenciação()

    elif opção_escolhida == 6:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        RADICIAÇÃO.Radiciação()

    elif opção_escolhida == 7:
        Tela_Modos_Jogo()

def Tela_Modos_Especiais():

    def Nome_Misto():
        modos_escolhidos = ARQUIVOS.Ler_Arquivo('Modos Misto')
        modos_de_jogo = ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Exponenciação', 'Radiciação']
        modos_de_jogo_escolhidos = []
        for modo in range(6):
            if modos_escolhidos[modo] == 'True':
                modos_de_jogo_escolhidos.append(modos_de_jogo[modo])
        if len(modos_de_jogo_escolhidos) > 0:
            return 'Misto'
        else:
            return 'XXXXXXX'

    def Nome_Fantasma():
        modos_escolhidos = ARQUIVOS.Ler_Arquivo('Modos Misto')
        modos_escolhidos.remove(modos_escolhidos[5])
        modos_de_jogo = ['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Exponenciação']
        modos_de_jogo_escolhidos = []
        for modo in range(5):
            if modos_escolhidos[modo] == 'True':
                modos_de_jogo_escolhidos.append(modos_de_jogo[modo])
        if len(modos_de_jogo_escolhidos) > 0:
            return 'Fantasma'
        else:
            return 'XXXXXXX'

    tela = ("----------------The-Calculator----------------\n"
            f"\033[95m(1) {Nome_Misto()}\n"
            f"\033[90m(2) {Nome_Fantasma()}\033[m\n"
            "(3) Voltar")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 3 or opção_escolhida == 1248163264 or opção_escolhida == 1123581321:
                if opção_escolhida == 1 and Nome_Misto() == 'XXXXXXX':
                    print('\033[91mNenhum modo selecionado!\033[m')
                elif opção_escolhida == 2 and Nome_Fantasma() == 'XXXXXXX':
                    print('\033[91mNenhum modo selecionado!\033[m')
                else:
                    break
            else:
                print("\033[91mDigite um número entre 1 e 3!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        MISTO.Misto()

    elif opção_escolhida == 2:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        FANTASMA.Fantasma()

    elif opção_escolhida == 1248163264:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        MINI_GAMES.Dobro_Em_Dobro()

    elif opção_escolhida == 1123581321:
        ARQUIVOS.Animação_Carregando('Carregando', 2, 'Carregar')
        MINI_GAMES.Fibonacci()

    elif opção_escolhida == 3:
        Tela_Modos_Jogo()

def Tela_Configurações():
    tela = ("----------------The-Calculator----------------\n"
            f"(1) Quantidade de Questões [{ARQUIVOS.Ler_Arquivo('Quantidade')}]\n"
            f"(2) Número Mínimo e Máximo [{ARQUIVOS.Ler_Arquivo('Dificuldade')[0]}][{ARQUIVOS.Ler_Arquivo('Dificuldade')[1]}]\n"
            f"(3) Casas decimais da Divisão [{ARQUIVOS.Ler_Arquivo('Decimais')}]\n"
            f"(4) Modos no misto\n"
            "(5) Voltar")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 5:
                break
            else:
                print("\033[91mDigite um número entre 1 e 5!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        Tela_Quantidade_Questões()
    if opção_escolhida == 2:
        Tela_Dificuldade()
    if opção_escolhida == 3:
        Tela_Casas_Decimais()
    if opção_escolhida == 4:
        Tela_Modos_Misto()
    if opção_escolhida == 5:
        PRINCIPAL.Principal()

def Tela_Quantidade_Questões():
    while True:
        try:
            quantidade_escolhida = int(input("Digite a quantidades de questões que você quer: "))
            if 1 <= quantidade_escolhida <= 100:
                break
            else:
                print("\033[91mDigite um número entre 1 e 100!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()


    ARQUIVOS.Adicionar_Arquivo('Quantidade', conteúdo_quantidade=quantidade_escolhida)
    Tela_Configurações()

def Tela_Dificuldade():
    while True:
        try:
            número_mínimo = int(input("Número mínimo: "))
            if 0 <= número_mínimo <= 1000:
                break
            else:
                print("\033[91mDigite um número entre 0 e 100!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    while True:
        try:
            número_máximo = int(input("Número máximo: "))
            if número_mínimo <= número_máximo <= 100:
                break
            else:
                print(f"\033[91mDigite um número entre {número_mínimo} e 100!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    ARQUIVOS.Adicionar_Arquivo('Dificuldade', conteúdo_dificuldade_mínimo=número_mínimo, conteúdo_dificuldade_máximo=número_máximo)
    Tela_Configurações()

def Tela_Casas_Decimais():
    while True:
        try:
            casas_decimais = int(input("Casa decimais: "))
            if 0 <= casas_decimais <= 3:
                break
            else:
                print("\033[91mDigite um número entre 0 e 3!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    ARQUIVOS.Adicionar_Arquivo('Decimais', conteúdo_decimais=casas_decimais)
    Tela_Configurações()

def Tela_Modos_Misto():
    valores = ARQUIVOS.Ler_Arquivo('Modos Misto')
    adição = valores[0]
    subtração = valores[1]
    multiplicação = valores[2]
    divisão = valores[3]
    exponenciação = valores[4]
    radiciação = valores[5]
    cores = list()

    for valor in valores:
        if valor == 'True':
            cores.append(92)
        if valor == 'False':
            cores.append(91)
    tela = ("----------------The-Calculator----------------\n"
            f"(1) \033[{cores[0]}m[Adição]\033[m         | (5) \033[{cores[4]}m[Exponenciação]\033[m\n"
            f"(2) \033[{cores[1]}m[Subtração]\033[m      | (6) \033[{cores[5]}m[Radiciação]\033[m\n"
            f"(3) \033[{cores[2]}m[Multiplicação]\033[m  | (7) Voltar\n"
            f"(4) \033[{cores[3]}m[Divisão]\033[m        |")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 7:
                break
            else:
                print("\033[91mDigite um número entre 1 e 7!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        if valores[0] == 'True':
            adição = False
        else:
            adição = True
    elif opção_escolhida == 2:
        if valores[1] == 'True':
            subtração = False
        else:
            subtração = True
    elif opção_escolhida == 3:
        if valores[2] == 'True':
            multiplicação = False
        else:
            multiplicação = True
    elif opção_escolhida == 4:
        if valores[3] == 'True':
            divisão = False
        else:
            divisão = True
    elif opção_escolhida == 5:
        if valores[4] == 'True':
            exponenciação = False
        else:
            exponenciação = True
    elif opção_escolhida == 6:
        if valores[5] == 'True':
            radiciação = False
        else:
            radiciação = True
    elif opção_escolhida == 7:
        Tela_Configurações()

    ARQUIVOS.Adicionar_Arquivo('Modos Misto', adição=adição, subtração=subtração, multiplicação=multiplicação, divisão=divisão, exponenciação=exponenciação, radiciação=radiciação)
    Tela_Modos_Misto()

def Tela_Estatísticas():
    estatísticas = ARQUIVOS.Ler_Arquivo(tipo='Estatísticas')
    tela = ("----------------The-Calculator----------------\n"
            f"Questões respondidas: {estatísticas[0]}\n"
            f"Questões acertadas: {estatísticas[1]}\n"
            f"Questões erradas: {estatísticas[2]}\n"
            "(1) Voltar")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 1:
                break
            else:
                print("\033[91mDigite o número 1!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        PRINCIPAL.Principal()

def Tela_Sem_Conta():
    tela = ("----------------The-Calculator----------------\n"
            "(1) Login\n"
            "(2) Cadastrar\n"
            "(3) Voltar")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 3:
                break
            else:
                print("\033[91mDigite um número entre 1 e 3!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        Tela_Login()
    if opção_escolhida == 2:
        Tela_Cadastrar()
    if opção_escolhida == 3:
        PRINCIPAL.Principal()

def Tela_Com_Conta(nome, senha):
    tela = ("----------------The-Calculator----------------\n"
            "(1) Informações da conta\n"
            "(2) Sair da conta\n"
            "(3) Voltar")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 3:
                break
            else:
                print("\033[91mDigite um número entre 1 e 3!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        Tela_Informações_Conta(nome, senha)
    if opção_escolhida == 2:
        ARQUIVOS.Adicionar_Arquivo(tipo='Conta_Logada', nome=None, senha=None)
        Tela_Sem_Conta()
    if opção_escolhida == 3:
        PRINCIPAL.Principal()

def Tela_Informações_Conta(nome, senha):
    tela = ("----------------The-Calculator----------------\n"
            f"Nome: {nome}\n"
            f"Senha: {senha}\n"
            "(1) Voltar")
    print(tela)

    while True:
        try:
            opção_escolhida = int(input("R: "))
            if 1 <= opção_escolhida <= 1:
                break
            else:
                print("\033[91mDigite o número 1!\033[m")
        except ValueError:
            print(f"\033[91mDigite um número válido!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    if opção_escolhida == 1:
        Tela_Com_Conta(nome, senha)

def Tela_Login():
    verificação_nome = ARQUIVOS.Ler_Arquivo(tipo='Conta_Nome')
    verificação_senha = ARQUIVOS.Ler_Arquivo(tipo='Conta_Senha')
    while True:
        try:
            nome = str(input("Digite o nome do usuário (s para sair): "))
            if nome in verificação_nome:
                break
            elif nome.upper() == 'S':
                Tela_Sem_Conta()
            else:
                print("\033[91mEssa conta não existe!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    senha = ''
    for contas in verificação_senha:
        if nome == contas[0]:
            while True:
                try:
                    senha = str(input("Digite a senha: "))
                    if senha == contas[1]:
                        break
                    else:
                        print("\033[91mSenha incorreta!\033[m")
                except KeyboardInterrupt:
                    print()
                    ARQUIVOS.Animação_Carregando('Saindo', 2)
                    exit()
            break

    ARQUIVOS.Adicionar_Arquivo(tipo='Conta_Logada', nome=nome, senha=senha)
    Tela_Com_Conta(nome, senha)

def Tela_Cadastrar():
    verificação_nome = ARQUIVOS.Ler_Arquivo(tipo='Conta_Nome')

    while True:
        try:
            nome = str(input("Digite um nome de usuário (s para sair): "))
            if nome not in verificação_nome:
                if len(nome) >= 3:
                    break
                elif nome.upper() == 'S':
                    Tela_Sem_Conta()
                else:
                    print('\033[91mSeu nome precisa possuir no mínimo 3 caracteres!\033[m')
            else:
                print("\033[91mEssa conta já existe!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    while True:
        try:
            senha = str(input("Digite uma senha (v para voltar): "))
            if len(senha) >= 8:
                break
            elif senha.upper() == 'V':
                Tela_Cadastrar()
            else:
                print('\033[91mSua senha precisa possuir no mínimo 8 caracteres!\033[m')
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    while True:
        try:
            verificação_senha = str(input("Digite a senha novamente (v para voltar): "))
            if verificação_senha == senha:
                break
            elif verificação_senha.upper() == 'V':
                Tela_Cadastrar()
            else:
                print("\033[91mAs senhas não são iguais!\033[m")
        except KeyboardInterrupt:
            print()
            ARQUIVOS.Animação_Carregando('Saindo', 2)
            exit()

    ARQUIVOS.Adicionar_Arquivo(tipo='Conta', nome=nome, senha=senha)
    print("\033[92mConta criada com sucesso!\033[m")
    Tela_Sem_Conta()
