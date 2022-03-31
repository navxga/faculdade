from time import sleep
print('=-'*15)
print('mAnálise de Notas')
print('=-'*15)

valores = []
indice = 1

w = int(input('Informe as notas '))

if w == 1:
    while True:
        n = float(input(f'Digite a {indice}ª nota: '))
        if n == -1:
            break
        valores.append(n)
        indice += 1
    print('Análise Finalizada...')
    sleep(1)

    # Cálculos
    '''qtd = len(valores)
    inversa = valores[::-1]
    soma = sum(valores)
    media = soma / qtd
    acima_media = len([n for n in valores if n >= media])
    abaixo_7 = [n for n in valores if n <= 7]
'''


    # Análise FINAL
    '''print('=-'*15)
    print(f'Foram lidos {qtd} valores.') # Quantidade de valores que foram lidos

    print('=-'*15)
    print(f'Ordem dos valores: {valores}') # Todos os valores na ordem em que foram informados

    print('=-'*15)
    print(f'Ordem inversa: {inversa}') # Todos os valores na ordem inversa em que foram informados

    print('=-'*15)
    print(f'Soma dos valores: {soma}') # Soma dos valores

    print('=-'*15)
    print(f'Média dos valores: {media}') # Média dos valores

    print('=-'*15)
    print('Obrigado, estarei aqui caso retorne.') # Encerramento do programa com uma mensagem
    print('=-'*15)'''
