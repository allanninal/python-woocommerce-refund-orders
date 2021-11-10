from woocommerce import API
import csv

wcapi = API(
    # Update here your website/domain
    url="https://www.example.com",
    # add here the WooCommerce REST API consumer key
    consumer_key="ck_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    # then the secret key
    consumer_secret="cs_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    wp_api=True,
    version="wc/v3"
)

# set to True if you also want the API to do the refund
api_refund = False

# open CSV for the orders
# 1 order id per line on the csv file

with open('orders.csv', 'r') as file:

    reader = csv.reader(file)
    for row in reader:

        order = wcapi.get("orders/" + row[0]).json()

        # we will be be doing the refund
        data = {
            "reason": "", # you can add reason here
            "amount": str(order['total']),
            "api_refund": api_refund
        }

        wcapi.post("orders/" + str(order['id']) + "/refunds", data).json()

        # and then update the status to refund
        data = {
            "status": "refunded"
        }

        wcapi.put("orders/" + str(order['id']), data).json()
