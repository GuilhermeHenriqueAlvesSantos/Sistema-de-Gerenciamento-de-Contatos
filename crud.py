def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Eduardo Freitas | Guilherme Santos | Marcus Divino          |')
    print('|                                                             |')
    print('| Versão 1.0 de 12/abril/2024                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar(agd):
    while True:
        nome = input("\nDigite o nome do contato que deseja procurar (ou '0' para sair): ")
        if nome == '0':
            break
        else:
            resposta = ondeEsta(nome, agd)
            achou = resposta[0]
            posicao = resposta[1]

            if achou:
                print('\nDados do Contato:')
                print('Nome.......:', agd[posicao][0])
                print('Aniversário:', agd[posicao][1])
                print('Endereço...:', agd[posicao][2])
                print('Telefone...:', agd[posicao][3])
                print('Celular....:', agd[posicao][4])
                print('e-mail.....:', agd[posicao][5])
            else:
                print("Contato não encontrado.")


def atualizar(agd):
    while True:
        nome = input("\nDigite o nome do contato que deseja atualizar (ou '0' para sair): ")
        if nome == '0':
            break
        else:
            resposta = ondeEsta(nome, agd)
            achou = resposta[0]
            posicao = resposta[1]

            if achou:
                while True:
                    opcoes_menu = ['Atualizar aniversário', 'Atualizar endereço', 'Atualizar telefone', 'Atualizar celular', 'Atualizar e-mail', 'Finalizar atualizações']
                    opcao = int(opcaoEscolhida(opcoes_menu))
                    if opcao == 6:
                        break
                    elif opcao == 1:
                        agd[posicao][1] = input("Novo aniversário: ")
                    elif opcao == 2:
                        agd[posicao][2] = input("Novo endereço: ")
                    elif opcao == 3:
                        agd[posicao][3] = input("Novo telefone: ")
                    elif opcao == 4:
                        agd[posicao][4] = input("Novo celular: ")
                    elif opcao == 5:
                        agd[posicao][5] = input("Novo e-mail: ")
                    else:
                        print("Opção inválida.")
            else:
                print("Contato não encontrado.")

def listar(agd):
    if not agd:
        print("Nenhum contato cadastrado.")
    else:
        print("\nLista de Contatos:")
        for contato in agd:
            print('\nNome.......:', contato[0])
            print('Aniversário:', contato[1])
            print('Endereço...:', contato[2])
            print('Telefone...:', contato[3])
            print('Celular....:', contato[4])
            print('e-mail.....:', contato[5])

def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=666
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')
