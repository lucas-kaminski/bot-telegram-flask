# README.dev
Neste arquivo terá informações pertinentes aos desenvolvedores do projeto.
Arquivo mutável com anotações, todos e passos a passos.

## Iniciando o ambiente
- [ ] Caso não tenha instalado, instala o pipenv de forma global
- [ ] Cria o ambiente virtual venv
- [ ] Inicializa o ambiente virtual
- [ ] Instala as dependências do projeto
- [ ] Cria e alimenta o .env a partir do .env.template
- [ ] Roda a criação de tabelas
- [ ] Inicializa o servidor
- [ ] Ativa o ngrok para porta 5000
- [ ] Pega o url do ngrok e setta os webhooks pela request
- [ ] Testa o ping

## Retomando o desenvolvimento
Refaz os passos acima a partir da inicialização do servidor

## Pontos a se desenvolver
- [ ] Importação de arquivos para o banco de dados
- [ ] Webhook da evermart
  - [ ] Histórico de ação do usuário (criar a possibilidade de trabalhar com qualquer gateway)
- [ ] Histórico de interação do usuário (ultima mensagem)
- [ ] CI/CD pro commit na master
  - [ ] gitbucket
    - [ ] commit
    - [ ] deploy
- [ ] Snippets

## Necessário um double check
- [ ] Fluxo do sistema stripe, está sendo feito o fluxo completo mas necessário validar cada ponto para evitar b.o (produtos (preço, recorrência, ...), assinaturas (ativa, desativa, vencida, ...), customers, etc...)
- [ ] As rotas de set coloquei em cada controller correspondente e a de atualização da moedas no internal (verificar um nome melhor para a rota que conversa com outros sistemas)
- [ ] Todos os tipos de updates do telegram, eventos da stripe e webhooks da evermart

## Possíveis desenvolvimento (analisar e se necessário, implementar)
- [ ] Não existe uma um arquivo de api da stripe, está sendo feito a manipulação direta no `import stripe`
- [ ] Webscrapping de noticias para o comando /news
- [ ] O comando /listarmoedas está salvando em JSON, ver se vai para banco
- [ ] Json de keyboards para padronização de botões de callback
- [ ] Migrar para FASTApi

## Comandos a serem implementados
- [x] /news
- [ ] /trades
- [x] /analise
  - [x] Banco de dados
  - [ ] API Binance
  - [ ] Pegar autor
- [ ] /carteiradotasso
  - [ ] Ver como vai funcionar o esquema de indicação
- [x] /fear
- [x] /help
- [x] /links
  - [ ] Ver quais links disponibilizarão para o usuário vip
- [x] /cadastro
- [x] /start
- [x] /suporte
- [x] /tutoriais

## Links

https://core.telegram.org/bots/api
https://core.telegram.org/bots/api#html-style

## Padrões de desenvolvimento

- Ao enviar um botão de callback, o valor de `callback_data` deve ser o caminho relativo a partir da pasta `commands` até o arquivo de callbackm, por exemplo: <br/>
`/news/financialNews` - Vai ser executado o módulo financialNews vindo do callback presente no botão presente no comando /news
- Para criar uma nova rota, deve se criar o controller e realizar a importação das classes do mesmo na `main.py`
- Para um middleware, se usa o método `before_request` da classe do app, e o arquivo deve ter uma validação das rotas através da condicional `if request.endpoint == 'route_name':`

## Comandos úteis
### Desenvolvimento
<!-- table -->
| CMD | Descrição |
| ------ | ---------- |
| `python -m venv venv` | Criação do ambiente virtual do python. |
| `venv/Scripts/Activate (windows) ou source venv/bin/activate (linux)` | Ativa o ambiente virtual do python (windows). |
| `pip install pipenv` | Instala o administrador de packages. |
| `python -m pipenv install` | Instala as dependências do sistema ou se passar um pacote, instala só ele. |
| `python -m pipenv run dev` | Inicialização do server em localhost. |
| `python -m pipenv run recreate_database` | Script de drop e recreate do banco de dados. |
| `python -m pipenv run formatter` | Formatação padrão no código. |

### Deploy
| CMD | Descrição |
| ------ | ---------- |
| `git push heroku master` | Envia o projeto para a heroku. |
| `heroku config:set STRIPE_WEBHOOK_SECRET_KEY=whsec_` | Define as variáveis de ambiente no heroku. |
| `heroku logs --tail` | Verifica o log do projeto. |
