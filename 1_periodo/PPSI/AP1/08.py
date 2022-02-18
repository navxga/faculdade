from time import sleep


print('=-'*15)
print('\033[32mAnálise de Notas\033[m')
print('=-'*15)

valores = []
indice = 1

choice = int(input('[ \033[32m1\033[m] Informe as notas \n[\033[32m-1\033[m] Sair \nQual a sua escolha?\033[32m '))

if choice == 1:
    while True:
        n = float(input(f'\033[mDigite a {indice}ª nota:\033[32m '))
        if n == -1:
            break
        valores.append(n)
        indice += 1
    print('Análise Finalizada...')
    sleep(1)

    # Cálculos
    qtd = len(valores) # quantidade
    inversa = valores[::-1] # ordem inversa
    soma = sum(valores) # soma
    media = soma / qtd # média
    acima_media = len([n for n in valores if n >= media]) # acima da média
    abaixo_7 = [n for n in valores if n <= 7] # abaixo de sete

    # Análise FINAL
    print('\033[32m=-\033[m'*15)
    print(f'Foram lidos {qtd} valores.') # Quantidade de valores que foram lidos

    print('\033[32m=-\033[m'*15)
    print(f'Ordem dos valores: {valores}') # Todos os valores na ordem em que foram informados

    print('\033[32m=-\033[m'*15)
    print(f'Ordem inversa: {inversa}') # Todos os valores na ordem inversa em que foram informados

    print('\033[32m=-\033[m'*15)
    print(f'Soma dos valores: {soma}') # Soma dos valores

    print('\033[32m=-\033[m'*15)
    print(f'Média dos valores: {media}') # Média dos valores

    print('\033[32m=-\033[m'*15)
    print('\033[35mObrigado, estarei aqui caso retorne.') # Encerramento do programa com uma mensagem
    print('\033[32m=-\033[m'*15)
else:
    print('\033[32m=-\033[m'*15)
    print('Obrigado, estarei aqui caso retorne.') # Encerramento do programa com uma mensagem
    print('\033[32m=-\033[m'*15)
