domingo, 24 de abril/2022

# Interface com o ambiente

### Objetivos
- Criar um esboço da interface com o cliente
- Ajudar na identificação dos comportamentos de uma aplicação
- Estruturar o fluxo de dados e o fluxo de controle 

## Sintaxe para desenhar/criar uma ICA (Interface Com o Ambiente)
- Aqui estarão as formas e símbolos que representam o que terá na interface:

### Fluxo de Dados
![image](https://user-images.githubusercontent.com/87860884/164999205-62e58bd7-4966-4e27-a7f4-466072aecffb.png)

### Fluxo de Controle
![image](https://user-images.githubusercontent.com/87860884/164999257-7044a947-e78b-42bf-a442-9808662f1aa8.png)

### Exemplo:

![image](https://user-images.githubusercontent.com/87860884/164999329-157809f4-d470-4dfc-8060-4a02860fa037.png) ![image](https://user-images.githubusercontent.com/87860884/164999374-733c9800-e3b8-4096-9795-0872f2f0aa6d.png)

<br><br><br>

# Tipos de Dados
- **Dado** é a representação de uma grandeza ou característica de algum elemento
    - Exemplo: temos o NOME dele como um DADO importante.

- **Tipos de Dados** definem qual representação vai definir o dado
    - Exemplo: IDADE de uma pessoa é representada por um NÚMERO NATURAL

## Os tipos de dados 
![image](https://user-images.githubusercontent.com/87860884/164999637-afadff5c-97ec-4e23-a3f3-53246097e3db.png)

## Abstração dos dados
- Envolve a organização dos dados de um problema em representações estruturadas e significativas para o negócio
    - Exemplo: um ALUNO é representado pelo seu RA(registro acadêmico) e seu NOME 
    - ![image](https://user-images.githubusercontent.com/87860884/164999753-ca232b71-df99-4d24-b6dd-7fef85b17ddb.png)

<br><br><br>

# O Caso IMC

- IMC - Índice de Massa Corporal
- Para saber se uma pessoa está no peso ideal vamos utilizar o IMC
- O método foi desenvolvido por *Lambert Quételet* no fim do século XIX
- ![image](https://user-images.githubusercontent.com/87860884/165000903-c0a27cad-4222-4260-92af-a3492de737f8.png)

## Fase de Análise do IMC
- Vamos seguir com:
    - Modelo de domínio
    - ICA
    - Lista de requisitos 

### Modelo de Domínio
![image](https://user-images.githubusercontent.com/87860884/165000997-75aabdfa-57da-43d7-9d5d-71588522ae42.png)

### ICA
![image](https://user-images.githubusercontent.com/87860884/165001021-239a0ef2-ee42-4561-a79f-d070d6bf87be.png)

### Lista de Requisitos
- **Peso** <br>
É um numero real que pode variar de [40.0 .. 160.0]

- **Altura** <br>
É um número real que pode variar de [1.4 .. 2.0]

- **Regra do negócio** <br>
É representada pela fórmula <br>
![image](https://user-images.githubusercontent.com/87860884/165001166-fff82207-0300-43d4-b718-7792e8400082.png)

- **Resultados** <br>
Podem ser:
    - Menor IMC possível ==> (40 / (1.4 * 1.4)) = 20.41
    - Maior IMC possível ==> (160 / (2 * 2)) = 40.0
    - Mensagem de erro: "Não foi possível calcular o IMC"
