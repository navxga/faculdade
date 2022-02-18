total = 0
for nota in range(1, 5):
    valor = float(input(f'{nota}ª nota: '))
    total += valor
media = total / 4
print(f'A sua média foi {media}')
