salario = float(input('Digite o seu salário: R$'))

if salario <= 280:
    aumento = salario*20/100
    reajuste = salario + aumento 
    print(f'O seu salário de R${salario:.2f} recebeu um aumento de 20%.') 
    print(f'O valor desse aumento: R${aumento:.2f} \nSeu novo salário é de R${reajuste:.2f}')

if 280 < salario <= 700:
    aumento = salario*15/100
    reajuste = salario + aumento
    print(f'O seu salário de R${salario:.2f} recebeu um aumento de 15%.') 
    print(f'O valor desse aumento: R${aumento:.2f} \nSeu novo salário é de R${reajuste:.2f}')

if 700 < salario <= 1500:
    aumento = salario*10/100
    reajuste = salario + aumento
    print(f'O seu salário de R${salario:.2f} recebeu um aumento de 10%.') 
    print(f'O valor desse aumento: R${aumento:.2f} \nSeu novo salário é de R${reajuste:.2f}')

if salario > 1500:
    aumento = salario*5/100
    reajuste = salario + aumento
    print(f'O seu salário de R${salario:.2f} recebeu um aumento de 5%. ')
    print(f'O valor desse aumento: R${aumento:.2f} \nSeu novo salário é de R${reajuste:.2f}')