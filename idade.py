while True:
    idade = int(input('Informe sua idade: '))

    if idade >= 18:
        retorno = 'Maior de idade'
    else:
        retorno = 'Menor de idade'

    print(retorno)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()

    if continuar in ['NÃO','NAO','N']:
        print('Programa encerrado...')
        break