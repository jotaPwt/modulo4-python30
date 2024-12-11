def soma(x,y):
    soma = x + y
    print(soma)

def subtração(x, y):
    sub = x - y
    print(sub)

for n in range(0,4):
    n1 = int(input('digite um numero: '))
    n2 = int(input('digite um numero: '))
    print('soma')
    soma(n1, n2)
    print('subtração')
    subtração(n1, n2)

    
    pergunta = input('Deseja fazer mais uma conta? s/n')
    if pergunta == 'n':
        break
    elif pergunta == 's':
        pass
    