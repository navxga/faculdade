print('Calcule seu peso!')
h = float(input('Digite a sua altura, em metros: '))
ph = (72.7 * h) - 58
pm = (62.1 * h) - 44.7
print(f'Se você for homem, seu peso ideal é: {ph:.1f}kg. Se for mulher: {pm:.1f}kg')