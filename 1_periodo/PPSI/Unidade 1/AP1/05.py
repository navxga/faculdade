n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda: '))
media = (n1 + n2)/2
if 7 <= media < 10:
    print(f'Aprovado! \nSua média foi: {media}')
if media < 7:
    print(f'Reprovado! \nSua média foi: {media}')
if media == 10:
    print(f'Aprovado com Distinção! \nSua média foi: {media}')