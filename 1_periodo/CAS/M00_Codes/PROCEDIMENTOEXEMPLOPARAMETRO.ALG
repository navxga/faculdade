Algoritmo "ProcedimentoExemploParametro"

PROCEDIMENTO multi (x, y: inteiro)
   VAR
   aux: inteiro

   INICIO
   aux <- x * y
   res <- aux
FIMPROCEDIMENTO

Var
res, n, m: inteiro

Inicio
ESCREVA("Digite um n�mero: ")
LEIA(n)
ESCREVA("Digite outro n�mero: ")
LEIA(m)
multi(n, m)
ESCREVA(res)

Fimalgoritmo