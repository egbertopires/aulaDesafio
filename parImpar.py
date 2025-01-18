numero = int(input('Inserir um número inteiro: '))

divisao = numero % 2

def parImpar(valorUm,valorDois):
    if valorUm == 0:
        return f'O número {valorDois} é par'
    else:
        return f'O número {valorDois} é ímpar'

print(parImpar(divisao,numero))