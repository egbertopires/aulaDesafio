tabuada = int(input('Qual tabuada deseja? '))

valoresTabuada = []
saida = f'Tabuada do número {tabuada}\n'
for valores in range (1,11):
    multiplicacao = tabuada * valores
    valoresTabuada.append(multiplicacao)
    saida += f'** {tabuada} x {valores} = {multiplicacao}\n'
print(saida[:-1])