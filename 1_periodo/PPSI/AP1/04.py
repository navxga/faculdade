ph = int(input('Quanto você ganha por hora? R$'))  # ph = por hora
# nh = número de horas
nh = int(input('Quantas horas você trabalhou esse mês? '))
bruto = ph * nh
liquido = bruto - (bruto*24/100)
print(f'Salário bruto: R${bruto:.2f}')
print(f'IR(11%): R${bruto*11/100:.2f}')
print(f'INSS(8%): R${bruto*8/100:.2f}')
print(f'Sindicato(5%): R${bruto*5/100:.2f}')
print(f'O seu Salário Líquido foi: R${liquido:.2f}')