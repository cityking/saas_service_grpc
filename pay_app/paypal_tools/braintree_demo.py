import braintree
access_token = 'access_token$sandbox$75fbzm74qvfgxx94$fe0240140bf4fb6e346876064e54bf85'
gateway = braintree.BraintreeGateway(access_token=access_token)

def client_token():
    client_token = gateway.client_token.generate()
    return client_token

def create_purchase(amount, payment_method_nonce, order_id, descriptor):
    result = gateway.transaction.sale({
        "amount" : amount,
        "merchant_account_id": "USD",
        "payment_method_nonce" : payment_method_nonce,
        "order_id" : order_id,
        "descriptor": {
          "name":descriptor 
        },
        "shipping": {
          "first_name": "Jen",
          "last_name": "Smith",
          "company": "Braintree",
          "street_address": "1 E 1st St",
          "extended_address": "Suite 403",
          "locality": "Bartlett",
          "region": "IL",
          "postal_code": "60103",
          "country_code_alpha2": "US"
        },
        "options" : {
          "paypal" : {
            "custom_field" : "PayPal custom field",
            "description" : "Description for PayPal email receipt"
          },
        }
    })
    if result.is_success:
        "Success ID: ".format(result.transaction.id)
    else:
        format(result.message)
