# teste-pratico <p>
<h2>Back-End</h2>
<h3>Banco de dados</h3>
Iniciei criando o banco de dados e optei por utilizar CSV, já que os dados a serem utilizados são de cunho público e de escala pequena, visto que a aplicação desse projeto se enquadra a apenas um usuário e os petshops próximos à sua localização não podem alcançar números expressivos. Seria possível modelar um banco de dados SQL para essa aplicação porém eu optei por não fazê-lo visto que essa solução performa bem e demanda menos code time<p>
Decidi modular meu banco da sequinte forma:
Dentro da pasta DB existem 3 arquivos petshop.csv, pricewkday.csv, pricewknd.csv. Nesses arquivos constam todas as informações pertinentes ao uso do programa. 
<li>petshop.csv: Nesse arquivo consta o ID(Primary Key), o nome da lógica(único) e a distância da loja</li>
<li>pricewkday.csv: Nesse arquivo costa o Shop_ID(Foreign Key do ID), little(preço para pets pequenos) e big(preço para pets grandes)</li>
<li>pricewknd.csv: Nesse arquivo costa o Shop_ID(Foreign Key do ID), little(preço para pets pequenos ou fator de porcentagem), big(preço para pets grandes ou fator de porcentagem) e percentage (valor binário que define se a loja usa percentual ou não como fator de aumento)</li><p><p>
Escolhi fazer essa abordagem pois tratar os dados dessa forma relacional com o ID de cada loja é eficiente para fazer buscas e possibilita em uma implementação futura a adição de mais lojas e a alteração dos preços das já cadastradas.<p>
<h3>Client</h3>
Após a criação do banco de dados modulei o meu código de forma que ficasse organizado e tentei seguir o SOLID à risca.<p>
Sendo assim esses são os arquivos presentes dentro do meu diretório Client:<p>
<ul>
  <li>
    <h4>db.py:</h4> Nesse arquivo consta todas as funções que se comunicam diretamente com o banco de dados e toda a configuração de path para que opere corretamente. Existe duas funções nesse script getsingledata() e getallids(). A primeira recebe como parametro um id e retorna todos os dados referentes à ele no objeto data, já a segunda retorna uma lista de strings com todos os ids presentes no banco.
  </li>
  <li>
    <h4>classes.py:</h4> Nesse arquivo estão as classes que foram utilizadas no programa. A primeira é a classe data. Esse objeto possui tipagem forte para o armazenamento dos dados de forma eficiente e a minimização de erros ela possui os atributos id(int), name(str), priceweekdays(dict), priceweekend(dict), distance(float), percentage(str). Além desses atributos, possui também um método simples porém útil usespercentage(self), esse método simplesmente retorna true caso a loja utilize porcentagem nos preços de final de semana e retorna false caso ela não use. Além desse objeto também existe a classe WrongPasswordError(Exception), que existe apenas para tratar exceções de erro de senha.
  </li>
  <li>
    <h4>utils.py:</h4> Nesse arquivo constam os utilitarios que realizam funções lógicas dentro do programa, são elas: <p></p>
    <b>isweekday(year : str, month : str, day : str) -> bool.</b> Essa função retorna true se a data for um dia da semana e false se não for, além disso ela tem um raise de um ValueError caso os dados fornecidos sejam impossíveis.<p></p>
    <b>getsingleprice(id : str, weekday : bool, quantity : Dict[str,int]) -> tuple[float,float, str].</b> Essa função utiliza das funções do db.py e dos métodos da classe data para cálcular o preço da lavagem em um petshop, retornando uma tupla com o preço, a distância e o nome do petshop. <p></p>
    <b>findbetterprice(budgets : list[tuple[float,float,str]]) -> dict.</b>b> Essa função recebe uma lista de tuplas no padrão da saída da função getsingleprice e retorna em um dicionário apenas o nome e o preço da melhor entre as filtradas.<p></p>
    <b>checkpassword(password : str) -> bool.</b> Essa função recebe uma string de senha e retorna true caso ela esteja correta e false em caso contrário.<p></p>
    Nessas funções existem raises for exepctions que são tratadas posteriormente. A função findbetter price funciona utilizando a ordenação nativa do python e eu não considero que isso causará algum problema de performance já que o banco de dados não é extenso.
  </li>
  <li>
    <h4>app.py:</h4> Nesse arquivo consta as rotas do Flask, framework que utilizei, e basicamente funciona com API's RESTful para realizar operações. No momento só foi implementada uma, responsável por encontrar o estabelecimento com o melhor preço, porém da forma que o código foi separado fica descomplicada a implementação de novas API's caso se faça necessário no futuro. Por exemplo se o cliente quiser adicionar uma loja nova que abriu na região ou deletar uma que fechou ou até mesmo atualizar os preços isso pode ser implementado. Além disso, nessa parte do programa também são tratadas as exceções e o recebimento de requests do lado do servidor.
  </li>
</ul>
