ph = int(input('Quanto você ganha por hora? R$')) # ph = por hora
nh = int(input('Quantas horas você trabalhou esse mês? ')) # nh = número de horas

bruto = ph * nh
liquido = bruto - (bruto * 24/100)
ir = bruto * 11/100 # 11%
inss = bruto * 8/100 # 8%
sind = bruto * 5/100 # 5%

print(f'Salário bruto: R${bruto:.2f}')
print(f'IR(11%): R${ir:.2f}')
print(f'INSS(8%): R${inss:.2f}')
print(f'Sindicato(5%): R${sind:.2f}')
print(f'O seu Salário Líquido foi: R${liquido:.2f}')