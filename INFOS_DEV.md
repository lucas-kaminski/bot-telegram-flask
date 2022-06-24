## Pontos a se desenvolver


## Necessário um double check
- [ ] Fluxo do sistema stripe, está sendo feito o fluxo completo mas necessário validar cada ponto para evitar b.o (produtos (preço, recorrência, ...), assinaturas (ativa, desativa, vencida, ...), customers, etc...)
- [ ] As rotas de set coloquei em cada controller correspondente e a de atualização da moedas no internal (verificar um nome melhor para a rota que conversa com outros sistemas)

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
