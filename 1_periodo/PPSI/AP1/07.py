n = int(input('Qual número, entre 1 e 10, você deseja ver a tabuada? '))

if 1 <= n <= 10:
    print('Tabuada de 5:')
    print(f'{n}  x  1 = {n}')
    print(f'{n}  x  2 = {n*2}')
    print(f'{n}  x  3 = {n*3}')
    print(f'{n}  x  4 = {n*4}')
    print(f'{n}  x  5 = {n*5}')
    print(f'{n}  x  6 = {n*6}')
    print(f'{n}  x  7 = {n*7}')
    print(f'{n}  x  8 = {n*8}')
    print(f'{n}  x  9 = {n*9}')
    print(f'{n}  x 10 = {n*10}')
else:
    print('Este número não está entre 1 e 10!')