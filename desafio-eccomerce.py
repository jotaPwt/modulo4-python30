# ***3 - a > cumprimentar usuário b_> fazer compra de um produto c_> finalizar compra e escolher a forma de pagamento*** 

# ***4 -  Funções -  Variáveis locais -  Condicionais -  Loops - Listas -  Dicionários***

def comprimento(nome):
    print('Olá seja bem vindo(a)', nome)



def compra():
    carrinho = []
    fazer_pedido = input('Deseja fazer um pedido? s/n: ')
    while fazer_pedido == 's':

        escolha = input('Digite o nome do produto que voce deseja: ')
        carrinho.append(escolha)
        print(carrinho)
        fazer_pedido = input('Deseja adicionar mais algum produto? s/n')
        
    else:
        print('Até mais')

    print(f'Seu carrinho é {carrinho}')
    
    
def pagamento():
    print('''
          Escolha a forma de pagamento
            1 - CD
            2 - CC
            3 - PIX
            4 - DINHEIRO
        ''')
    
    pagamento = int(input('digite forma de pagammento de acordo com o código de cada opção'))

    if pagamento == 1:
        print('CARTÃO DE CRÉDITO ESCOLHIDO')
    elif pagamento == 2:
        print('CARTÃO DE DÉBITO ESCOLHIDO')
    elif pagamento == 3:
        print('PIX ESCOLHIDO')
    elif pagamento == 4:
        print('DINHEIRO ESCOLHIDO')
    else:
        ('Digite algo valido')

    pagar = input('''
                PAGAR - s
                VOLTAR - n
            ''')
    
    if pagar == 's':
        print('Pagamento Concluido, volte semmpre!')
    elif pagar == 'n':
        print('Que pena, Tchau')
    


def mercado():

    nome = input('Digite seu nome: ')
    comprimento(nome)

    compra()
    pagamento()

    sair_do_sistema = input('')


mercado()