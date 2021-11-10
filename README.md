What Is This?
-------------

This python script refund orders with a option of using API Refund of the Payment Gateway.

How To Use This
---------------

1. Create `orders.csv` with all the order ids, one order id per line.
2. Run `pip install woocommerce`
3. Run `pip install csv`
4. Make sure you have the WooCommerce REST API consumer and secret keys
5. Set `api_refund` to `True` if you also want the API for the Payment Gateway used to do the refund.
6. Run `python woocommerce-python-refund-orders.py`
