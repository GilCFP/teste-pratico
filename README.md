
- [1. Resumo](#1-resumo)
- [2. Utilização](#2-utilização)
- [3. Implementação](#3-implementação)
- [4. Back-End](#4-back-end)
  - [4.1. Banco de dados](#41-banco-de-dados)
  - [4.2. Client](#42-client)
- [5. Front-End](#5-front-end)
  - [5.1. SRC](#51-src)
  - [5.2. public](#52-public)
  - [5.3. eslint](#53-eslint)
- [6. Considerações Finais](#6-considerações-finais)
## 1. Resumo
Para o back end foi utilizado python, com o framework Flask APIs RESTfull. No front foi utilizado React e o banco de dados foi organizado em arquivos CSV.
## 2. Utilização
O usuário abre a página inicial e nela consta um formulário, no qual ele fornecerá os dados(data, quantidade de cães pequenos, quantidade de cães grandes), após pressionar enviar aparecerá abaixo do formulário o nome do melhor Pet shop e o preço total.

## 3. Implementação
1. Inicializando backend
   1. Clone esse repositório
   2.  No seu terminal, inicialize o ambiente virtual que se encontra no diretório backend/venvp utilizando o script activate dentro de backend/venvp/Scripts
   3.  No ambiente virtual, navegue até o dir "backend/client"
   4.  Já na pasta backend, insira o comando "flask run"
   5.  O servidor back end deve ser iniciado em local host na porta 5000.

2. Inicializando o frontend
   1. No seu terminal navegue até a pasta frontend
   2. Execute o comando npm run
   3. O frontend deve ser iniciado em local host na porta 3000

## 4. Back-End
O backend foi feito em python, organizado de forma modular para facilitar manutenções, seguindo os principios SOLID e tipado para otimizar os gastos de memória.

### 4.1. Banco de dados
Iniciei criando o banco de dados e optei por utilizar CSV, já que os dados a serem utilizados são de cunho público e de escala pequena, visto que a aplicação desse projeto se enquadra a apenas um usuário e os petshops próximos à sua localização não podem alcançar números expressivos. Seria possível modelar um banco de dados SQL para essa aplicação porém eu optei por não fazê-lo visto que essa solução performa bem e demanda menos code time.<p>
Decidi modular meu banco da sequinte forma:
Dentro da pasta DB existem 3 arquivos petshop.csv, pricewkday.csv, pricewknd.csv. Nesses arquivos constam todas as informações pertinentes ao uso do programa.
- **petshop.csv:** Nesse arquivo consta o ID(Primary Key), o nome da lógica(único) e a distância da loja
- **pricewkday.csv:** Nesse arquivo costa o Shop_ID(Foreign Key do ID), little(preço para pets pequenos) e big(preço para pets grandes)
- **pricewknd.csv:** Nesse arquivo costa o Shop_ID(Foreign Key do ID), little(preço para pets pequenos ou fator de porcentagem), big(preço para pets grandes ou fator de porcentagem) e percentage (valor binário que define se a loja usa percentual ou não como fator de aumento)
Escolhi fazer essa abordagem pois tratar os dados dessa forma relacional com o ID de cada loja é eficiente para fazer buscas e possibilita em uma implementação futura a adição de mais lojas e a alteração dos preços das já cadastradas.<p>

### 4.2. Client

Nesse diretório estão presentes os módulos e o app que faz o host do servidor:<p>

- #### db.py:
  - Esse arquivo armazena todas as funções que se comunicam diretamente com o banco de dados e toda a configuração de path para que opere corretamente. Existe duas funções nesse script getsingledata() e getallids(). A primeira recebe como parametro um id e retorna todos os dados referentes à ele no objeto data, já a segunda retorna uma lista de strings com todos os ids presentes no banco.

- #### classes.py:
  - Nesse arquivo estão as classes que foram utilizadas no programa. A primeira é a classe data. Esse objeto possui tipagem forte para o armazenamento dos dados de forma eficiente e a minimização de erros ela possui os atributos id(int), name(str), priceweekdays(dict), priceweekend(dict), distance(float), percentage(str). Além desses atributos, possui também um método simples porém útil usespercentage(self), esse método simplesmente retorna true caso a loja utilize porcentagem nos preços de final de semana e retorna false caso ela não use. Além desse objeto também existe a classe WrongPasswordError(Exception), que existe apenas para tratar exceções de erro de senha.

- #### utils.py:
  - Nesse arquivo constam os utilitarios que realizam funções lógicas dentro do programa, são elas: <p></p>
    1.**isweekday(year : str, month : str, day : str) -> bool.**  Essa função retorna true se a data for um dia da semana e false se não for, além disso ela tem um raise de um ValueError caso os dados fornecidos sejam impossíveis.<p></p>
    2.**getsingleprice(id : str, weekday : bool, quantity : Dict[str,int]) -> tuple[float,float, str].**  Essa função utiliza das funções do db.py e dos métodos da classe data para cálcular o preço da lavagem em um petshop, retornando uma tupla com o preço, a distância e o nome do petshop. <p></p>
    3.**findbetterprice(budgets : list[tuple[float,float,str]]) -> dict.b>**  Essa função recebe uma lista de tuplas no padrão da saída da função getsingleprice e retorna em um dicionário apenas o nome e o preço da melhor entre as filtradas.<p></p>
    4.**checkpassword(password : str) -> bool.**  Essa função recebe uma string de senha e retorna true caso ela esteja correta e false em caso contrário.<p></p>
    Nessas funções existem raises para as exepctions, que são tratadas posteriormente. A função findbetterprice funciona utilizando a ordenação nativa do python e eu não considero que isso causará algum problema de performance já que o banco de dados não é extenso.

- #### app.py:
  - Nesse arquivo constam as rotas do Flask, framework que utilizei, com API's RESTful. Somente uma foi implementada, responsável por encontrar o estabelecimento com o melhor preço, porém da forma que o código foi separado fica é possível e rápida a implementação de novas API's caso seja necessário no futuro. Por exemplo, se o cliente quiser adicionar uma loja nova que abriu na região ou deletar uma que fechou ou até mesmo atualizar os preços isso pode ser implementado. Além disso, nessa parte do programa também são tratadas as exceções e devolve códigos HTTP adequados a cada caso na response.

## 5. Front-End
Para o front end foi utilizado React como demandado e o UX e UI feito foi simples, já que a aplicação não apresenta muitos recursos. No front também existe a verificação dos dados fornecidos pelo usuário impedindo-o de fornecer dados errados e a utilização de uma senha para comunicação com a api, para que ela não seja consumada por pessoas não autorizadas. Vale mencionar que esse é o meu primeiro contato com React, logo foi desafiador aprender e criar de forma rápida.

### 5.1. SRC
Nesse diretório existem os seguintes arquivos relacionados ao Front-End:
- **form.js:** nesse script consta o formulário que será utilizado para obter os dados do usuário. O formulário foi montado utilizando recursos do react-bootstrap e possui uma função DataForm(), responsável por fazer a request na API com os dados do usuário e retorná-las para a função isertData().
- **App.js:** esse script carrega a página index.html. Nele a estrutura básica é um container com duas divs, uma com os components do form.js e a outra inicialmente vazia que será preenchida ao receber a resposta da API. Nesse script foi utilizado useState e useEffect. O useState foi usado como hooker para a response da request na API e para o efeito de fade na inserção das informações.
- **App.css** estilização da página
Existem outros scripts mas não houve implementação significativa de lógica por minha parte neles. Utilizei o react-bootstrap para ajudar na estilização dos components e responsividade, porém precisei implementar algumas alterações diretas na estilização para deixar com a aparencia desejada.

### 5.2. public
Nesse diretório constam o ícone utilizados para a pagina e o index.html, além do manifest.json e robots.txt

### 5.3. eslint
Foi utilizado eslint durante a criação desse projeto para auxiliar com imports e sintaxe adequada.

## 6. Considerações Finais
Foi gratificante fazer esse teste prático e pude aprender bastante durante a execução dele, gostaria de adicionar novas funcionalidades como a alteração de dados no banco caso necessário porém eu fiquei sem tempo, pois passei muito tempo aprendendo o básico do React. Acredito que pude mostrar os meus conhecimentos e espero que a minha implementação tenha agradado. Eu priorizei o backend pois é a área que possuo mais afinidade e interesse, porém me esforcei para fazer um front end decente também. Obrigado por considerar a minha candidatura.
