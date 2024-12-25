import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_KEY


def product_sales(product_name="Test Product", product_price=1000):
    stripe_prod_obj = stripe.Product.create(name=product_name)
    stripe_prod_obj_id = stripe_prod_obj.id

    stripe_price_obj = stripe.Price.create(
        currency="usd",
        unit_amount=product_price,
        product=stripe_prod_obj_id
    )

    stripe_price_id = stripe_price_obj.id

    base_end_point = "http://127.0.0.1:8000"
    success_url = f"{base_end_point}/purchase/start/"
    cancel_url = f"{base_end_point}/purchase/stop/"

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": stripe_price_id,
                "quantity": 1
            }
        ],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url
    )

    # print('this is url::\n', checkout_session.url)
