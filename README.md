# Bot do Telegram da Financial Move

O sistema foi feito em python, utilizando o flask para o desenvolvimento da api do sistema e a biblioteca mysql para conexão com o banco de dados.

Inicial foi inspirado no atual [bot da Financial](https://t.me/Cryptointeliggencebot), com a implementação de todos os comandos e a expansão conforme demanda.

## Estrutura

Na pasta raiz `./` terá informações pertinentes ao sistema, como configurações do editor, git, etc...

Dentro da pasta `./src/` está orquestado a lógica do sistema e as rotas.

No arquivo `main.py` está instanciado o servidor flask, neste arquivo também tem de estar explicitado todas as rotas presentes na controller.

Na pasta `api` estarão todas as funções que fazem requisições para api externas.

Na pasta `commands` estarão todos os comandos aceito pelo bot do Telegram. <br/>
Para os arquivos em pastas, ao ser importado o arquivo, será chamado o método `__init__.py` que inicia o comando base, os outros arquivos na pasta são referentes a callbacks. <br/>
Para os arquivos com nome de comando, será chamado eles diretamente e os mesmos não possuem callback.

Na pasta `controllers` estarão todas as rotas do sistema e suas tratativas.

Na pasta `database` estará o arquivo `connection.py` que contém as configurações de conexão e execução no banco de dados. <br/>
Nesta pasta também há o arquivo `script.py` que contém o script de drop e recreate do banco de dados e a pasta queries.
Na pasta `queries` estarão todos as funções que executam um SQL no banco, separado entre cada tabela.

Na pasta `middleware` estará todas as funções que tratam as requisições do sistema.

Já a pasta `server` possui o objeto do servidor.

Por fim, a pasta `utils` contém todas as funções que auxiliam no desenvolvimento do sistema, como validações e formatações.

## Possíveis fluxos do servidor

### **Telegram**
O [bot do telegram](https://t.me/WTLLBot) é o responsável pelo principal fluxo do sistema. <br/>
Ao receber uma mensagem por chat direto ou em um canal, o telegram irá enviar um webhook com as informações para a rota `/telegram` do sistema. <br/>
Essa rota possui um middleware que irá primeiramente o tipo de mensagem recebida, atualmente se aceita três tipos, sendo eles: </br>
- `message`: Mensagem de um chat direto, irá validar o usuário e executar o comando. <br/>
- `callback`: Callback do click de um botão enviado para o cliente, irá validar o usuário e executar o callback presente dentro de uma pasta na pasta `commands`.<br/>
- `channel_post`: Mensagem de um canal, irá verificar se o canal está salvo no banco de dados. <br/>

### **Stripe**
a

## Padrões de desenvolvimento

- Ao enviar um botão de callback, o valor de `callback_data` deve ser o caminho relativo a partir da pasta `commands` até o arquivo de callbackm, por exemplo: <br/>
`/news/financialNews` - Vai ser executado o módulo financialNews vindo do callback presente no botão presente no comando /news
- Para criar uma nova rota, deve se criar o controller e realizar a importação do mesmo na `main.py`
- Para um middleware, se usa o método `before_request` da classe do app, e o arquivo deve ter uma validação das rotas através da condicional `if request.endpoint == 'route_name':`

## Deploy
O deploy foi realizado na heroku, no [link](https://secure-fortress-69045.herokuapp.com/).

## Comandos úteis
<!-- table -->
| CMD | Descrição |
| ------ | ---------- |
| `python .\src\main.py` | Inicialização do server em localhost. |
| `python .\src\database\script.py` | Script de drop e recreate do banco de dados. |
