valorPagamento = 0 #determinar o valor a ser pago por uma prestação de uma conta
valorPrestacao = float(input('Digite o valor da prestação: R$'))
diasAtraso = int(input('Digite o número de dias em atraso: '))

if diasAtraso > 0:
    valorPagamento = valorPrestacao + (valorPrestacao * 0.03)
    valorPagamento = ((diasAtraso * 0.001) * valorPagamento) + valorPagamento
    jurSimples = diasAtraso * 0.001 + 0.03
    print(f'\nJuros diários compostos: R${valorPagamento:.2f}\n')
    print(f'Juros simples sobahsdasdasre o total: R${jurSimples * valorPrestacao + valorPrestacao:.2f}\n')
else:
    valorPagamento = valorPrestacao
    print(f'\nPagamento sem atraso! \nValor a ser pago: R${valorPagamento:.2f}')