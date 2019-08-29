from pay_app.models import PayPalPay
def create():
    pay = PayPalPay.objects.all().first()
    item = dict(name='测试商品', price=10, currency='USD', quantity=10)
    payment = pay.create_payment([item], 100, '7777777')
    return payment
if __name__ == '__main__':
    payment = create()
