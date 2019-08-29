import paypalrestsdk
from paypalrestsdk import Order

client_id = 'AcEDucP7esIyXneuPawC-yOSGVI4V5VWbiGtCxXiylrtFE0UvZtftQtZHaLSqJTj08pB1CICdjS6bKAs'
client_secret = 'EOjJK6dli_PAW6POxRUBPyazS_V0s8X7mldU7HOX-MxEj0YP0hqrCt8JGzR2p4_B-1bR-Yxl4bHNAbGF'
return_url = 'http://localhost:3000/payment/execute'
cancel_url = 'http://localhost:3000/'

paypalrestsdk.configure({
  'mode': 'sandbox', #sandbox or live
  'client_id': client_id,
  'client_secret': client_secret })

def create_payment(name, price, quantity, total, description=''):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": return_url,
            "cancel_url": cancel_url},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": name,
                    "sku": name,
                    "price": price,
                    "currency": "USD",
                    "quantity": quantity}]},
            "amount": {
                "total": total,
                "currency": "USD"},
            "description": description}]})
    if payment.create():
      print("Payment created successfully")
      #payment.execute({"payer_id": "DUFRQ8GWYMJXC"})
    else:
      print(payment.error)
    
    for link in payment.links:
        if link.rel == "approval_url":
            # Convert to str to avoid Google App Engine Unicode issue
            # https://github.com/paypal/rest-api-sdk-python/pull/58
            approval_url = str(link.href)
            print("Redirect for approval: %s" % (approval_url))
            return approval_url

def payment_excute(paymentId, PayerID):
    payment = paypalrestsdk.Payment.find(paymentId)
    
    if payment.execute({"payer_id": PayerID}):
      print("Payment execute successfully")
      return True
    else:
      print(payment.error) # Error Hash

if __name__ == '__main__':
    #url = create_payment('测试支付', 10, 10, 100)
    import pdb;pdb.set_trace()
