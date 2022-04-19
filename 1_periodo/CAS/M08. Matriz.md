terça-feira, 19 de abril/2022

# Estrutura Homogênea Multidimensional

- Matriz é um **vetor** dos **vetores**
- Possui várias dimensões. Vetores são, na verdade, **matrizes de uma única dimensão**
- Cada item da matriz é acessado por um índice

## Matriz
- São referenciadas através de suas dimensões (linhas e colunas)
- MxN
  - **M** é a dimensão **horizontal** (quantidade de **linhas**)
  - **N** é a dimensão **vertical** (quantidade de **colunas**)
> ### Exemplo:
> 
> ![image](https://user-images.githubusercontent.com/87860884/164011313-96d67e20-9c99-4427-a131-dd0cfbd863c5.png)

### Declaração

nomeDaVariavel: **vetor** [ValorInicialLinhas..ValorFinalLinhas, ValorInicialColunas..ValorFinalColunas] **de** tipoDaVariavel
> ### Exemplo:
> `notas: vetor[1..50, 1..4] de inteiro`

### Para usar o vetor é necessário usar 2 estruturas de repetição:

![image](https://user-images.githubusercontent.com/87860884/164013841-14318cfc-a03f-4f5f-9fba-598adaab91d6.png)

> ### Exemplo:

```
PARA i DE 1 ATE 50 FACA
   ESCREVA("Aluno(a) número", i)
   PARA j DE 1 ATE 4 FACA
     ESCREVA("Digite a", j, "ª nota:")
     LEIA (notas[i, j])
    FIMPARA
 FIMPARA
 ```
