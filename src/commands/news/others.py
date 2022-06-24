from api.telegram import updateMessage


class Others:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]
        message_id = kwargs["message_id"]

        print("others")

        text = "📰 <b>NOTÍCIAS GERAIS</b> \n\n📰"
        text += '📰 <a href="https://livecoins.com.br/deputado-quer-vetar-justica-de-acessar-chave-privada-de-criptomoedas/)">Deputado quer vetar justiça de acessar chave privada de criptomoedas</a>\n'
        text += "Um deputado federal no Brasil quer vetar a justiça brasileira de acessar a chave privada de criptomoedas de pessoas que devam dinheiro. Dessa forma, ele pretende alterar o Código de Processo Civil e demais leis relacionadas para isso.\n\n"
        text += '📰 <a href="https://cointelegraph.com.br/news/new-listings-brasil-bitcoin-lists-2-new-cryptocurrencies-and-bluebenx-lists-14-new-digital-assets)">Duas exchanges nacionais anunciam a listagem de 16 novas criptomoedas para os usuários brasileiros</a>\n'
        text += "Novas listagens: Brasil Bitcoin lista 2 novas criptomoedas e BlueBenx lista 14 novos ativos digitais\n\n"
        text += '📰 <a href="https://portaldobitcoin.uol.com.br/nona-maior-baleia-de-bitcoin-do-mundo-compra-7-000-btcs-durante-queda/)">Nona maior baleia de bitcoin do mundo compra 7.000 BTCs durante queda</a>\n'
        text += "Enquanto as sardinhas se desesperam com o preço do Bitcoin (BTC) caindo para a região dos US$ 22 mil, as baleias vão às compras. A nona maior baleia —  termo que se refere a um investidor que detém grandes quantias de criptomoedas — de bitcoin do mercado adquiriu 7.\n\n"
        text += '📰 <a href="https://cointelegraph.com.br/news/nexo-offers-to-buy-out-celsius-loans-amid-withdrawal-suspension)">Nexo se oferece para comprar empréstimos da Celsius em meio a suspensão de saques</a>\n'
        text += "A plataforma Nexo poderia resgatar os clientes da Celsius após “o que parece ser a insolvência da Celsius Network”.\n\n"
        text += '📰 <a href="https://livecoins.com.br/microstrategy-acumula-us-1-bilhao-em-perdas-apos-queda-do-bitcoin/)">MicroStrategy acumula US$ 1 bilhão em perdas após queda do Bitcoin</a>\n'
        text += "A MicroStrategy, empresa pública com o maior número de BTC em caixa, está com uma perda não realizada de US$ 1 bilhão (R$ 5,1 bi) devido a forte queda do Bitcoin nesta semana. Apesar disso, seu fundador e CEO, Michael Saylor, segue confiante no futuro do Bitcoin.\n\n"
        text += '📰 <a href="https://livecoins.com.br/ufmg-usara-blockchain-no-combate-de-tdah/)">UFMG usará blockchain no combate de TDAH</a>\n'
        text += "A Universidade Federal de Minas Gerais (UFMG), assinou um acordo com uma empresa para pesquisar sobre como utilizar a tecnologia blockchain no diagnóstico do Tratamento de Déficit de Atenção e Hiperatividade (TDAH). Essa doença afeta pessoas por todo o mundo em sua capacidade de aprender e se concentrar em tarefas.\n\n"
        text += '📰 <a href="https://livecoins.com.br/binance-nao-dara-suporte-a-novo-recurso-da-litecoin-ltc/)">Binance não dará suporte a novo recurso da Litecoin (LTC)</a>\n'
        text += "A Binance, exchange de criptomoedas fundada por Changpeng Zhao, anunciou nesta segunda-feira (13) que não trabalhará com depósitos e saques de Litecoin (LTC) que usarem o recurso MimbleWimble Extension Blocks (MWEB).\n\n"
        text += '📰 <a href="https://portaldobitcoin.uol.com.br/corretora-crypto-com-demite-260-funcionarios-devido-a-crise-no-mercado-de-criptomoedas/)">Corretora Crypto.com demite 260 funci\nonários devido à crise no mercado de criptomoedas</a>\n'
        text += "A Crypto.com irá demitir 260 pessoas, cerca de 5% de seus funcionários corporativos, à medida que os mercados continuam caindo, de acordo o CEO da empresa, Kris Marszalek.\n\n"
        text += '📰 <a href="https://cointelegraph.com.br/news/brazil-in-nft-game-heroes-of-metaverse-raises-r-14-million-reserva-distributes\n-nfts-for-free-and-le-helps-women-enter-the-market)">Brasil em NFT: Game "Heroes of Metaverse" levanta R$ 14 milhões, Reserva distribui NFTs de graça, e Livia Elektra ajuda mulheres a entrar no mercado</a>\n'
        text += "Apesar da queda do mercado de criptomoedas, mercado de NFTs brasileiro não para e novos projetos vêm sendo desenvolvidos.\n\n"
        text += '📰 <a href="https://cointelegraph.com.br/news/edward-snowden-defends-cryptocurrencies-as-a-form-of-payment-and-reveals-a\nnonymous-use-of-bitcoin-to-pay-for-web-hosting)">Edward Snowden defende criptomoedas em pagamentos e diz que críticos deveriam entender melhor a indústria cripto</a>\n'
        text += "Denunciante estadunidense exilado na Rússia usou a criptomoeda para custear servidores que vazaram documentos da NSA.\n\n"

        print(text)
        updateMessage(user["TELEGRAM_ID"], message_id, text, parse_mode="HTML")
