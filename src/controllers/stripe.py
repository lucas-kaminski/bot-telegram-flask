from flask import Flask, request, Response, jsonify
from flask_restx import Api, Resource
import json
import stripe

import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.environ.get("STRIPE_API_KEY")

from dateutil.relativedelta import relativedelta
from datetime import date

from server.instance import server
from middleware.validateWebhookFromStripe import validateWebhookFromStripe
from database.queries.products import selectAllProducts, updateProduct, selectProduct
from database.queries.users import updateUser, selectUser
from database.queries.vip_users import selectVipUser, insertVipUser, updateVipUser

app, api = server.app, server.api


@api.route("/stripe/sync/products")
class SyncStripeProducts(Resource):
    def post(self):
        products_from_database = selectAllProducts()
        products_from_stripe = stripe.Product.list()

        new_products = []
        registered_products = []

        for product in products_from_database:
            if product["STRIPE_ID"] is None:
                new_products.append(product)
            else:
                registered_products.append(product)

        # TODO: produtos desativados

        for new_product in new_products:
            stripe_product = stripe.Product.create(
                name=new_product["NAME"],
                active=True,
                description=new_product["DESCRIPTION"]
                if new_product["DESCRIPTION"] != ""
                else None,
                metadata={
                    "id": new_product["ID"],
                },
                default_price_data={
                    "currency": "BRL",
                    "unit_amount_decimal": str(new_product["PRICE"]).replace(".", ""),
                    "recurring": {
                        "interval": "month",
                        "interval_count": new_product["VALIDITY_IN_MONTHS"],
                    },
                },
            )

        return jsonify({"status": "ok"})


@api.route("/stripe/set/webhook")
class SetWebhook(Resource):
    def post(self):
        if os.environ.get("ENVIRONMENT") == "production":
            return Response(status=403)
        else:
            print("Setting webhook in development mode")
            url = request.get_json()["url"]

            old_webhooks = stripe.WebhookEndpoint.list()
            for i in old_webhooks["data"]:
                stripe.WebhookEndpoint.delete(i["id"])

            endpoint = stripe.WebhookEndpoint.create(
                url=url + "/stripe/webhook",
                enabled_events=["*"],
            )

            return endpoint["secret"]


app.before_request(validateWebhookFromStripe)


@api.route("/stripe/webhook")
class StripeWebhook(Resource):
    def post(self):
        event = request.args["event"]
        event_type = event["type"]

        if event_type == "customer.created":
            customer = event["data"]["object"]
            customer_database_id = customer["metadata"]["id"]
            updateUser(id=customer_database_id, stripe_id=customer["id"])
        elif event_type == "customer.deleted":
            customer = event["data"]["object"]
            customer_database_id = customer["metadata"]["id"]
            updateUser(id=customer_database_id, stripe_id=None)
        elif event_type == "product.created":
            product = event["data"]["object"]
            product_database_id = product["metadata"]["id"]
            updateProduct(id=product_database_id, stripe_id=product["id"])
        elif (
            event_type == "checkout.session.completed"
            or event_type == "checkout.session.async_payment_succeeded"
        ):
            session = event["data"]["object"]
            user = selectUser(stripe_id=session["customer"])
            vip_user = selectVipUser(user_id=user["ID"])
            subscription = stripe.Subscription.retrieve(session["subscription"])
            product = selectProduct(stripe_id=subscription["plan"]["product"])

            expiration_date = date.today() + relativedelta(
                months=+product["VALIDITY_IN_MONTHS"]
            )

            status = (
                "active" if session["payment_status"] == "paid" else "awaiting_payment"
            )
            if vip_user is None:
                insertVipUser(
                    user_id=user["ID"],
                    product_id=product["ID"],
                    expiration=expiration_date,
                    status=status,
                )
            else:
                updateVipUser(
                    id=vip_user["ID"], expiration=expiration_date, status=status
                )
        elif event_type == "invoice.paid":
            invoice = event["data"]["object"]
            user = selectUser(stripe_id=invoice["customer"])
            vip_user = selectVipUser(user_id=user["ID"])
            subscription = stripe.Subscription.retrieve(invoice["subscription"])
            product = selectProduct(stripe_id=subscription["plan"]["product"])
            expiration_date = vip_user["EXPIRATION"] + relativedelta(
                months=+product["VALIDITY_IN_MONTHS"]
            )
            updateVipUser(
                id=vip_user["ID"], expiration=expiration_date, status="active"
            )
        elif event_type == "customer.subscription.deleted":
            subscription = event["data"]["object"]
            user = selectUser(stripe_id=subscription["customer"])
            updateVipUser(id=user["ID"], status="canceled")
        else:
            print("Unknown event type: " + event_type)

        return jsonify(received=True)
