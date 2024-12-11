def mercado():
    pedidos = []
    fazer_pedido = input('Deseja fazer o pedido? s/n')
    while fazer_pedido == 's':

        escolha = input('Digite seu pedido: ')
        pedidos.append(escolha)
        print(pedidos)
        fazer_pedido = input('Deseja continuar? s/n')
        if fazer_pedido == 'n':
            print('Seu carrinho é:', pedidos)
        else:
            pass
    else:
        print('Até Logo')
        
mercado()




# print('''
        #     CARDÁPIO

        # 1 - arroz
        # 2 - feijão
        # 3 - ovo
        
        # ''')
        # escolha = int(input('DIGITE O CÓDIGO CORRESPONTENTE A CADA PRODUTO DESEJADO:'))