NULLABLE = {'null': True, 'blank': True}

"""def get_session(instance):
    " Функция возвращает сессию для оплаты "
    title_product = f"{instance.paid_lesson}" if instance.paid_lesson else ''

    product = stripe.Product.create(
        name=f'{title_product}'
    )

    price = stripe.Price.create(
        unit_amount=instance.payment_amount,
        currency='usd',
        product=f'{product.id}',
    )

    session = stripe.checkout.Session.create(
        success_url="http://example.com/success",
        line_items=[
            {
                'price': f'{price.id}',
                'quantity': 1,
            }
        ],
        mode='payment',
        customer_email=f'{instance.user.email}'

    )
    return session"""