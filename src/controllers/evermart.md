# Webhooks
[Link docs](https://ajuda.evermart.com.br/docs/sobre/integracoes/o-que-sao-e-como-usar-os-webhooks/) <br/>
[Link PDF](https://mega.nz/file/6Z1l3QjQ#69lPUFCh5vO8AXijxaIWLfNUpTBefYwq-YQpm-xbk68)

# Evento de pedido
Legenda: <br/>
 \*: INT <br/>
 \**: FLOAT <br/>

O que está separado a seguir é uma separação feita para facilitar a leitura da query. (by: Lucas Kaminski)

## Autenticação
hottok -> Cada conta possui um hottok único e essa é a principal garantia de que o post está sendo feito peloMy Checkout <br/>
transaction -> codigo da transação <br/>
xcod -> códigos customizados definido no link de venda <br/>
src -> códigos customizados definido no link de venda <br/>
hotkey -> Enviado apenas no caso de Sites de Membros (venda de acesso a conteúdo restrito). Trata-se do número de série único liberado para aquele comprador <br/>
sck -> Código de até 6 caracteres. Pode ser customizado pelo usuário para rastrear origens das vendas realizadas em seus checkouts <br/>
receiver_type -> Tipo do usuário receptor do evento gerado pelo webhook ('SELLER', 'AFFILIATE') <br/>
has_co_production -> Indica se o produto possui co-produção (true ou false) <br/>

## Comprador
### Dados
email <br/>
name <br/>
first_name <br/>
last_name <br/>
doc (999999999999999) <br/>
doc_type -> Tipo de documento do comprador (CPF/CNPJ/DNI..) <br/>
phone_local_code*  <br/>
phone_number* phone_checkout_local_code*  <br/>
phone_checkout_number* <br/>

### Endereço
address  <br/>
address_number  <br/>
address_country  <br/>
address_district  <br/>
address_comp <br/>
address_city  <br/>
address_state <br/>
address_zip_cod <br/>

## Produto
prod* -> Código do produto <br/>
prod_name -> Nome do produto <br/>
warranty_date -> Data de vencimento da garantia do produto adquirido <br/>
product_support_email ->  Email do suporte do produto  <br/>

## Compra
status ->  approved, canceled, billet_printed, refunded, dispute, completed, blocked, chargeback, delayed, expired, wayting_payment <br/>
purchase_date (1970-04-01T12:50:30Z) <br/>
confirmation_purchase_date (1970-04-01T12:50:30Z) <br/>

## Preço
original_offer_price** -> Preço original do produto  <br/>
currency -> Descrição da moeda (R$)  <br/>
currency_code_from -> Código da moeda de origem da transação (brl)  <br/>
currency_code_from_ -> Origem da moeda utilizada no pagamento da compra (BRL) <br/>
full_price** -> Valor total da compra <br/>
installments_number* -> números parcelas  <br/>

## Pagamento
transaction_ext -> Código de transação gerado pelo meio de pagamento externo <br/>
refusal_reason -> Texto de recusa do pagamento pela operadora <br/>
payment_engine -> 'mycheckout ', 'bcash','monthly', 'paypal', 'moip' <br/>
payment_type -> 'billet', 'credit_card', 'debit_card', 'bank_transfer', 'moip_balance', 'bcash_balance', 'paypal','order.checkout.mycheckout_balance' <br/>
productOfferPaymentMode -> 'pagamento_unico', 'multiplos_pagamentos','pagamento_vista '<br/>

## Oferta
off -> cód oferta <br/>
price** -> preço da oferta na compra <br/>

## Assinatura
name_subscription_plan -> venda de assinatura | subscriber_code -> código do assinante  <br/>
recurrency_period* -> é enviado sempre que a compra é do tipo assinatura e ele é enviado para notificação de compra e cancelamento. Os valores possíveis para este campo são 7, 30, 60, 90, 180 e 360 e esses valores representam a periodicidade em dias do pagamento da respectiva assinatura. O preenchimento desse campo leva em consideração o status da assinatura que é enviado no campo  'subscription_status' <br/>
recurrency* -> Período do pagamento em que o assinante atualmente está  <br/>
subscription_date_next_charge -> Data da próxima cobrança  <br/>
callback_type -> Tipo do callback: 1 -compra pagamento único; 2 -cancelamento assinatura  <br/>
subscription_status -> status da assinatura (active, canceled, past_due, expired, started, inactive)  <br/>
signature_status -> Status da assinatura ( 'Active', 'Inactive', 'Delayed', 'Canceled by client', 'Canceled by vendor', 'Canceled by admin', 'Expired', 'Started)  <br/>

## Afiliado
aff -> código afiliado <br/>
aff_name -> nome afiliado <br/>

## Comissões
cms_marketplace** <br/>
cms_vendor** <br/>
cms_aff** <br/>
aff_cms_rate_currency -> moeda de conversão <br/>
aff_cms_rate_commission** -> valor da comissão convertida  <br/>
aff_cms_rate_conversion** -> Taxa utilizada no momento da conversão  <br/>
cms_aff_currency -> Moedas da comissão do afiliado  <br/>

## Cupom
coupon_code -> código do cupom  <br/>

## Boleto
billet_url -> Link para reimprimir o boleto da compra  <br/>
billet_barcode -> Código de barras do boleto <br/>

## Produtor
producer_name -> nome do produtor  <br/>
producer_document -> documento do produtor  <br/>
producer_legal_nature -> Natureza jurídica  <br/>

## Ingressos
amount* -> Quantidade de e-tickets (ingressos)

<br/>
<br/>
<br/>
<br/>

# Abandono de carrinho
{<br/>
  "affiliate": "boolean",<br/>
  "hottok": "string",<br/>
  "userKey": "string",<br/>
  "productName": "string",<br/>
  "productId": "integer",<br/>
  "productUcode": "string",<br/>
  "productCategory": "integer",<br/>
  "buyerVO": { "name": "string", "email": "string", "phone": "string" },<br/>
  "hasNegotiate": "boolean",<br/>
  "subscriptionPlanId": "integer"<br/>
}<br/><br/>

<br/>
<br/>
<br/>
<br/>

# Troca de plano
{ <br/>
  "hottok": "string", <br/>
  "switchPlanDate": "datetime", <br/>
  "subscription": { <br/>
    "product": { "id": "integer", "name": "string" }, <br/>
    "recurrenceNumber": "integer", <br/>
    "status": "string", <br/>
    "subscriber": { <br/>
      "code": "string", <br/>
      "user": { "name": "string", "email": "string" } <br/>
    }, <br/>
    "plan": { <br/>
      "name": "string", <br/>
      "maxChargeCycles": "integer", <br/>
      "recurrencyPeriod": "integer", <br/>
      "offer": { "key": "string" }, <br/>
      "value": "float", <br/>
      "currencyCode": "string" <br/>
    } <br/>
  }, <br/>
  "newSubscriptionPlan": { <br/>
    "name": "string", <br/>
    "maxChargeCycles": "integer", <br/>
    "recurrencyPeriod": "integer", <br/>
    "offer": { "key": "string" }, <br/>
    "value": "float", <br/>
    "currencyCode": "string" <br/>
  }, <br/>
  "previousSubscriptionPlan": { <br/>
    "name": "string", <br/>
    "maxChargeCycles": "integer", <br/>
    "recurrencyPeriod": "integer", <br/>
    "offer": { "key": "string" }, <br/>
    "value": "float", <br/>
    "currencyCode": "string" <br/>
  } <br/>
} <br/><br/>

<br/>
<br/>
<br/>
<br/>

# Cancelamento de assinatura
{<br/>
  "hottok": "string",<br/>
  "subscriptionId": "integer",<br/>
  "subscriberCode": "string",<br/>
  "cancellationDate": "datetime",<br/>
  "userName": "string",<br/>
  "userEmail": "string",<br/>
  "actualRecurrenceValue": "float",<br/>
  "productName": "string",<br/>
  "subscriptionPlanName": "string",<br/>
  "dateNextCharge": "datetime"<br/>
}<br/><br/>

---

# Exemplo de requisição
## Compra de um produto com 7 dias de garantia, disponibilidade de 12 meses e valor de R$ 5,00. Oferta mensal do tipo de assinatura com dois dias de 2 teste.

1ª webhook (compra aceita) <br/>
hottok=62b48a465ee4be0ab8eeb62f&prod=62b4b85ba7eaa949f1962161&prod_name=ProdutoTesteWTLL&off=62b4ba2531e51931064ea3b4&price=0.00&aff=&aff_name=&email=lucas.kssilveira%40gmail.com&name=Lucas%20Kaminski%20Schimidt%20da%20Silveira&first_name=Lucas&last_name=Kaminski&doc=11674158920&phone_local_code=41&phone_number=998119091&phone_checkout_local_code=41&phone_checkout_number=998119091&address=&address_number=&address_country=Brasil&address_district=&address_comp=&address_city=&address_state=&address_zip_code=&transaction=PAY-QV7PK8ZG1ZSJ&xcod=&src=&utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=&status=approved&payment_engine=evermart&payment_type=credit_card&hotkey=&name_subscription_plan=Mensal&subscriber_code=96914&recurrency_period=30&cms_marketplace=0.00&cms_vendor=0.00&cms_aff=0.00&coupon_code=&callback_type=1&subscription_status=active&transaction_ext=PAY-QV7PK8ZG1ZSJ&sck=&purchase_date=2022-06-23T16%3A19%3A54.891Z&confirmation_purchase_date=2022-06-23T16%3A19%3A54.891Z&billet_url=&currency_code_from=BRL&currency_code_from_=BRL&original_offer_price=0.00&currency=BRL&signature_status=active&billet_barcode=&producer_name=Bruno%20Borelli&producer_document=140153427&producer_legal_nature=CPF&refusal_reason=&doc_type=CPF&full_price=0.00&warranty_date=2022-06-30T16%3A19%3A54.891Z&cms_aff_currency=BRL&product_support_email=lucas.kaminski.wtll%40gmail.com&amount=1&aff_cms_rate_currency=BRL&aff_cms_rate_commission=0.00&aff_cms_rate_conversion=&installments_number=1&has_co_production=true&productOfferPaymentMode=pagamento_vista&receiver_type=SELLER&subscription_date_next_charge=2022-07-26T00%3A00%3A00.000Z&order_bump=false&parent_purchase_transaction=PAY-QV7PK8ZG1ZSJ&order_bump_ids=&instagram=&quantityTickets=&order_id=62b4bcdad8742b4d96a46732

2º webhook (refund por ser periodo de teste) <br/>
hottok=62b48a465ee4be0ab8eeb62f&prod=62b4b85ba7eaa949f1962161&prod_name=ProdutoTesteWTLL&off=62b4ba2531e51931064ea3b4&price=0.00&aff=&aff_name=&email=lucas.kssilveira%40gmail.com&name=Lucas%20Kaminski%20Schimidt%20da%20Silveira&first_name=Lucas&last_name=Kaminski&doc=11674158920&phone_local_code=41&phone_number=998119091&phone_checkout_local_code=41&phone_checkout_number=998119091&address=&address_number=&address_country=Brasil&address_district=&address_comp=&address_city=&address_state=&address_zip_code=&transaction=PAY-QV7PK8ZG1ZSJ&xcod=&src=&utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=&status=refunded&payment_engine=evermart&payment_type=credit_card&hotkey=&name_subscription_plan=Mensal&subscriber_code=96914&recurrency_period=30&cms_marketplace=0.00&cms_vendor=0.00&cms_aff=0.00&coupon_code=&callback_type=1&subscription_status=active&transaction_ext=PAY-QV7PK8ZG1ZSJ&sck=&purchase_date=2022-06-23T16%3A19%3A54.891Z&confirmation_purchase_date=2022-06-23T16%3A19%3A54.891Z&billet_url=&currency_code_from=BRL&currency_code_from_=BRL&original_offer_price=0.00&currency=BRL&signature_status=active&billet_barcode=&producer_name=Lucas%20Kaminski&producer_document=140153427&producer_legal_nature=CPF&refusal_reason=&doc_type=CPF&full_price=0.00&warranty_date=2022-06-30T16%3A19%3A54.891Z&cms_aff_currency=BRL&product_support_email=lucas.kaminski.wtll%40gmail.com&amount=1&aff_cms_rate_currency=BRL&aff_cms_rate_commission=0.00&aff_cms_rate_conversion=&installments_number=1&has_co_production=true&productOfferPaymentMode=pagamento_vista&receiver_type=SELLER&subscription_date_next_charge=2022-07-26T00%3A00%3A00.000Z&order_bump=false&parent_purchase_transaction=PAY-QV7PK8ZG1ZSJ&order_bump_ids=&instagram=&quantityTickets=&order_id=62b4bcdad8742b4d96a46732

## Carrinho abandonado
{ <br/>
  "event": "CART_ABANDONED", <br/>
  "affiliate": false, <br/>
  "hottok": "62b48a465ee4be0ab8eeb62f", <br/>
  "productName": "ProdutoTesteWTLL", <br/>
  "productId": "62b4b85ba7eaa949f1962161", <br/>
  "productUcode": "62b4b85ba7eaa949f1962161", <br/>
  "productCategory": 0, <br/>
  "buyerVO": { <br/>
    "phone": "41 998119091", <br/>
    "name": "Lucas Kaminski Schimidt da Silveira", <br/>
    "email": "lucas.kssilveira@gmail.com" <br/>
  }, <br/>
  "hasNegotiate": false, <br/>
  "subscriptionPlanId": 96914 <br/>
} <br/>

## Assinatura cancelada
{ <br/>
  "hottok": "62b48a465ee4be0ab8eeb62f", <br/>
  "subscriptionId": 96921, <br/>
  "subscriberCode": 96921, <br/>
  "cancellationDate": "2022-06-23T19:38:39.173Z", <br/>
  "actualRecurrenceValue": 0, <br/>
  "productName": "ProdutoTesteWTLL", <br/>
  "subscriptionPlanName": "", <br/>
  "dateNextCharge": "2022-09-27T00:00:00.000Z" <br/>
} <br/>
