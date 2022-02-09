'''
3pt por vitória
1pt por empate
0pt por derrota

Dar um nome
Quantidade de: vitórias, empates e derrotas #qv, qe, qd
Quantidade de pontos totais no campeonato #qp
Quantidade de jogos disputados #qj
'''
print('Seja bem vindo ao sistema de Jogos do Campeonato')
nome = input('Qual o nome do seu time? ')
qv = int(input('Quantas vitórias o '+nome+' teve ? '))
qe = int(input('E empates? '))
qd = int(input('...Derrotas? '))

print('Certo... Calculando.')

qp = (qv*3 + qe)
qj = (qv + qe + qd)
print('Perfeito, aqui está: Seu time obteve {0} pontos, jogando {1} jogos'.format(qp, qj))

