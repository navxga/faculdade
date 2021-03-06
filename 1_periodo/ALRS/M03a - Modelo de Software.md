 sábado, 23 de abril/2022

![image](https://user-images.githubusercontent.com/87860884/164909938-364240cd-f243-4419-acf5-3124260ad3b1.png)


# Abstração

- É um processo mental que a gente usa, para poder enxergar as coisas. Podendo assim, destacar o que é mais relevante e o que não é
- Agora, o **Modelo**, ele é a materialização do meu pensamento em algum artefato. Seja ele um desenho, um texto, uma gravação de áudio...

![image](https://user-images.githubusercontent.com/87860884/164991992-b98ef91a-deb0-4324-b072-bb79d54657a1.png)

> ### Exemplo:
> Descrição de algo
>
> ![image](https://user-images.githubusercontent.com/87860884/164992123-bfe0c668-0373-4fed-8d8c-4c4cdc1206ef.png)
>
> Descrevendo essa caneta nós podemos dizer: Tem uma tampa, tem um corpo e é da cor azul
>
> Porém, essa descrição não tem um propósito, não tem um contexto, é **irrelevante**
> 
> No momento em que eu coloco um propósito, essa descrição muda, veja:
> - O propósito sendo: O Dono da papelaria
> - Como será que ele descreve essa caneta? O que é **relevante** pra ele?
> O custo da caneta. Qual é o lucro que eu vou ter com essa caneta. Se eu tenho essa caneta em estoque. Quem é o fornecedor dessa caneta...


## Representação do Modelo

Aqui a gente fez o modelo, ou seja, é a materialização da abstração que eu fiz (sobre a caneta)

![image](https://user-images.githubusercontent.com/87860884/164992366-3613e00c-b33d-4f9b-a1d2-24d9dfef2efc.png)

De um lado temos a descrição sem contexto, irrelevante
- a CANETA tem um TUBO e uma TAMPA

Do outro lado, a descrição do produto, do que realmente é relevante para o Dono da papelaria
- a CANETA é um PRODUTO e ele tem um PREÇO


                                                                                                                                         A M A Z O N A S



# Erros de Abstração

Aqui eu vou te mostrar os erros que você não pode cometer quando for materializar a sua abstração

## Elemento Omisso
- Ocorre quando você omite sem querer uma informação, seja por que você se esqueceu, ou achou que já tinha entendido...
- Como por exemplo: Vamos supor que você queira fazer a materialização de uma faixada de prédio.
- ![image](https://user-images.githubusercontent.com/87860884/164992901-b2e1addc-cba3-4fea-9692-bbd492a0908c.png)
- Como eu já falei, você consegue até dizer que isso é um prédio. Mas e quem ta vendo pela primeira vez
- Acontece que faltou um Elemento que foi omitido por você
- ![image](https://user-images.githubusercontent.com/87860884/164992948-d827eccf-3957-4e40-b775-efabd3b77d36.png)
- As janelas do prédio, agora sim isso é uma faixada de prédio!

## Elemento Detalhe
- Vamos continuar... Agora, você já antingiu o seu objetivo de materializar uma faixada de prédio. Todos já entenderam a sua ideia, porém, você quis desenhar mais. Adicionou uma cortina... Um **detalhe** que não faz diferença no objetivo principal: que é mostrar uma faixada de prédio
- ![image](https://user-images.githubusercontent.com/87860884/164993025-eed00f18-dd81-4cec-97ee-5d4c0e3d7cd4.png)
- Esse é o **Elemento Detalhe**, os detalhes que você continua passando, mesmo depois de alcançar o objetivo de ilustrar a sua ideia, tornam-se irrelevantes. Tome cuidado! Apenas o prédio com as janelas já era suficiente.

## Elemento Estranho
- "Olha! Eu quero mostrar pra vocês que lá dentro do prédio tem um chafariz"
- ![image](https://user-images.githubusercontent.com/87860884/164993150-c3422c94-1eb4-4be5-b968-ed7736d08134.png)
- Esse é o Erro de Abstração!
- Veja que, esse chafariz não tem nenhuma ligação relevante com a faixada do prédio
- O Elemento Estranho representa algo que, conforme eu vou desenvolvendo o meu sistema, eu vou encontrá-lo ali na frente
- Então, no primeiro instante que eu ainda estou conversando com o meu cliente, eu já estou dando sugestões de tecnologias... NÃO É O MOMENTO

## Elemento Alienígena
- ![image](https://user-images.githubusercontent.com/87860884/164993211-6865a0b5-93e2-4ac7-9ae2-40ade4de7e4d.png)
- O que que o Sol tem a ver com a faixada?
- NADA!
- É totalmente irrelevante ao contexto
- Isso nós chamamos de Elemento Alienígena





# Modelo de Domínio
- A modelagem de domínio é uma atividade para identificar os termos utilizados no projeto do software ou para construir o glossário do projeto
- Define os fundamentos de escopo e elementos para construção do uso do software
- Oferece um vocabulário comum para a comunicação entre os membros da equipe

## DCL (Diagrama de Classe)
- É um diagrama da UML (Linguagem de Modelagem Unificada), que usaremos neste contexto como uma ferramenta para desenhar o DOMÍNIO
- ![image](https://user-images.githubusercontent.com/87860884/164998396-a1fa660f-d273-43da-b59c-3f3a2e3da249.png)

### Elementos de uma DCL
![image](https://user-images.githubusercontent.com/87860884/164998432-f77253ec-45b4-4ceb-a04d-1568bb897796.png)

### Tipos de Ligação
![image](https://user-images.githubusercontent.com/87860884/164998446-f0d1938f-357e-4419-a2ab-5809da7c4974.png)
- Associação: Uma classe conversa e usa elementos de outra classe
- Dependência: Uma classe depende de outra para ser executada
    - Por exemplo: A classe MÁQUINA depende da classe PROGRAMA para a gente ter a COMPUTAÇÃO
- Agregação: Uma classe funciona como um container
    - Por exemplo: A classe A seria uma Garrafa, e a classe B seria a Água
- Composição: Representa a necessidade de existência. A classe A existe se a classe B existir
- Generalização: representa um "É um"
    - A classe B **É UM** representante da classe A 
    - Por exemplo: Classe A -> caneta e Classe B -> produto = A caneta É UM produto
