dadosVendedores = {}
salarioVendedor = []
i = 0

while i < 10:
    nomeVendedor = input('Nome: ')
    sal = input('Salário: R$')
    salarioVendedor.append(sal)
    dadosVendedores[f'{nomeVendedor}'] = (salarioVendedor[i])
    i += 1

contagem = [0] * i

print('\nRelação de funcionários - Salário:')

for a, b in dadosVendedores.items(): #A = Nome, B = Salário
    indice = int(b) // 100 - 1
    indicemax = len(contagem) - 1
    indice = min(indice, indicemax)
    contagem[indice] += 1
    print(f'{a}: R${b}')

#print('Teste contagem:')
#print(contagem)

i = 1
ii = 0

print('\nGrupos de salário entre R$100 e acima de R$1000:')
for a in contagem:
    print(f'Grupo de R${i}00+: {contagem[ii]}')
    i += 1
    ii += 1


