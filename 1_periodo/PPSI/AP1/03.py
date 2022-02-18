h = float(input('Digite a sua altura, em metros: '))
sx = str(input('Você é homem ou mulher? h/m: ')).lower().strip()
if sx == 'h':
    peso = 72.7 * h - 58
    print(f'O seu peso ideal é {peso:.2f}kg.')
else:
    peso = 62.1 * h - 44.7
    print(f'O seu peso ideal é {peso:.2f}kg.')
