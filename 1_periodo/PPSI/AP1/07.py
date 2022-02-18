n = int(input('Gerador de Tabuada. Digite um número: '))

if 0 < n < 11:
    for t in range(1, 11):
        print(f'{n} x {t:2} = ', n * t)
else:
    print('Erro! O número digitado não está entre 1 e 10.')
