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
ESCREVA("Digite um número: ")
LEIA(n)
ESCREVA("Digite outro número: ")
LEIA(m)
multi(n, m)
ESCREVA(res)

Fimalgoritmo