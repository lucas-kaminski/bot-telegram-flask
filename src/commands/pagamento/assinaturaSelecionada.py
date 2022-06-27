from api.telegram import updateMessage
from database.queries.products import selectProduct

from dateutil.relativedelta import relativedelta
from datetime import date


class AssinaturaSelecionada:
    def __init__(self):
        pass

    def run(self, **kwargs):
        id_product = kwargs["callback_info"]
        product = selectProduct(id_product)

        user = kwargs["user"]
        message_id = kwargs["message_id"]

        buttons = [
            [
                {
                    "text": "Confirmar ✅",
                    "callback_data": f"/pagamento/confirmar:{id_product}",
                }
            ],
            [{"text": "Retornar 🔙", "callback_data": "/pagamento/cartaoOuBoleto"}],
            [{"text": "Cancelar ❌", "callback_data": "/pagamento/cancelar"}],
        ]

        duration_formatted = (
            f'{product["VALIDITY_IN_MONTHS"]} mes'
            if product["VALIDITY_IN_MONTHS"] == 1
            else f'{product["VALIDITY_IN_MONTHS"]} meses'
        )
        price_formatted = f'R$ {str(product["PRICE"]).replace(".",",")}'
        month = date.today() + relativedelta(months=+product["VALIDITY_IN_MONTHS"])
        month_formatted = f"{month.day}/{month.month}/{month.year}"

        text = "Você está adquirindo o seguinte conteúdo: \n\n"
        text += f'{product["NAME"]}\n\n'
        text += "Período de assinatura do Grupo VIP da Financial Move\n"
        text += f"Duração de {duration_formatted}\n"
        text += f"Valor: {price_formatted}\n"
        text += f"Validade: {month_formatted}\n\n"
        text += "Confirma a sua escolha?"

        updateMessage(user["TELEGRAM_ID"], message_id, text, buttons)
