from api.telegram import sendMessage

import time


class Tutoriais:
    def __init__(self):
        pass

    def run(self, **kwargs):
        user = kwargs["user"]

        # Mensagem 1
        text = "Fala meu rei, seja muito bem vindo ao Bot da Financial Move \n\n"
        text += "Aqui no Bot é onde você acessa os trades do Tasso em tempo real \n\n"
        text += "Segue o passo a passo pra você entender como funciona para acessar o melhor do VIP (Vídeo no botão abaixo)"

        buttons = [
            [
                {
                    "text": "📺 Instruções para acessar",
                    "url": "https://financialmove.com.br/como-acessar",
                }
            ]
        ]

        sendMessage(user["TELEGRAM_ID"], text, buttons)
        time.sleep(1)

        # Mensagem 2
        text = "➡ Passo 1: \n"
        text += "Clique no botão abaixo para ver os tutoriais e entender como funcionam as informações do Bot"

        buttons = [
            [
                {
                    "text": "📺 Ver tutorial do bot",
                    "url": "https://financialmove.com.br/tutoriais-bot",
                }
            ]
        ]

        sendMessage(user["TELEGRAM_ID"], text, buttons)
        time.sleep(1)

        # Mensagem 3
        text = "➡ Passo 2: \n"
        text += "Digite o comando  /links \n"
        text += "Com esse comando você acessa o CANAL VIP e a ÁREA VIP \n"
        text += "- No CANAL VIP você tem acesso à conversa onde o Tasso conta em detalhes os bastidores de toda sua estratégia \n"
        text += "- Na ÁREA VIP você acessa os cursos e conteúdos *BÔNUS* da assinatura do VIP \n"
        text += "(Ambos são exclusivos para assinantes do VIP)"

        sendMessage(user["TELEGRAM_ID"], text)
        time.sleep(1)

        # Mensagem 4
        text = "➡ Passo 3: \n"
        text += "Digite o comando /trades \n"
        text += "Com esse comando você acessa todos os trades disponíveis no momento \n"
        text += "Lembrando que operamos SWING TRADE, ou seja, não abrimos trades todos os dias, ok? \n"
        text += "Se você ainda é um usuário Gratuito do Bot, pode aguardar algum trade gratuito ou assinar o VIP para liberar todos os trades na hora \n"

        sendMessage(user["TELEGRAM_ID"], text)
        time.sleep(1)

        # Mensagem 5
        text = "➡ Passo 4: \n"
        text += "Digite o comando /pagamento \n"
        text += "Com esse comando você acessa a área de pagamento \n"
        text += "Na área de pagamento você pode fazer sua assinatura ou mudar de plano de forma fácil e automática \n"

        sendMessage(user["TELEGRAM_ID"], text)
        time.sleep(1)

        # Mensagem 6
        text = "E por fim, você pode usar o comando /help para descobrir todos os comandos do bot! \n\n"
        text += "Um abraço do Tasso e de toda a equipe da Financial! \n\n"
        text += "Somos a #revolução Cripto 📈"

        buttons = [
            [
                {
                    "text": "📳 Falar com o suporte",
                    "url": "https://financialmove.com.br/andreimeajuda",
                }
            ]
        ]
        sendMessage(user["TELEGRAM_ID"], text, buttons)
        time.sleep(1)
