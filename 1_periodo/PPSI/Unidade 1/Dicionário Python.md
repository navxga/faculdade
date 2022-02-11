01/02/2022 <br>
Unigranrio
# Dicionário unordered dos Códigos Python

1. `print()`
Imprime a mensagem especificada para o Console.
EX: print('Meu primeiro código em Python') # exibe na tela: Meu primeiro código em Python

2. `type()`
Especifica o tipo de um objeto.
EX: a = 4.5 
print(type(a)) # exibe na tela: float

3. `print(x[y])`
Sendo x uma variável;
y um número inteiro;
Esses colchetes servem para acessar apenas o caractere de número y
EX: print('Python'[3]) # exibe na tela: h

4. `strip()`
Remove qualquer espaço em branco do começou ou do fim
EX: a = "   Programando em Python   "
print(a.strip()) # exibe na tela: Programando em Python

5. `len()`
Retorna o número de caracteres. O tamanho de uma string
EX: a = "Programando em Python"
print(lent(a)) # exibe na tela: 21

6. `lower()`
Retorna a string em letras minúsculas
EX: a = "Programando em Python"
print(a.lower()) # exibe na tela: programando em python

7. `upper()`
Retorna a string em letras maiúsculas
EX: a = "Programando em Python"
print(a.upper()) # exibe na tela: PROGRAMANDO EM PYTHON

8. `replace()`
Substitui uma string por outra string
EX: a = "Python"
print(a.replace("P","C")) # exibe na tela: Cython

9. `split()`
Separa as string em substrings
EX: a = "Banana, Mamão, Jabuticaba"
print(a.split(",")) # exibe na tela: ['Mamão', ' Banana', ' Jabutacaba']

10. `input()`
Faz uma pausa no programa, e espera a entrada do usuário no terminal
EX: print("Digite seu nome:")
#vamos supor q vc escreveu Lyan
a = input()
print("Muito bom te conhecer, "+a) #exibe na tela: Muito bom te conhecer, Lyan
