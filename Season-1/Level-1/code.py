'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_TOTAL = 1000000
MAX_ITEM_AMOUNT = 100000
MIN_ITEM_AMOUNT = 0
MAX_QUANTITY = 100
MIN_QUANTITY = 0


def validorder(order: Order):
    payment_amount = Decimal('0.0')
    product_amount = Decimal('0.0')

    for item in order.items:
        if item.type == 'payment':
            if -MAX_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT:
                payment_amount += Decimal(str(item.amount))
        elif item.type == 'product':
            if (type(item.quantity) is int) and (MIN_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT) and (MIN_QUANTITY <= item.quantity <= MAX_QUANTITY):
                product_amount += Decimal(str(item.amount * item.quantity))
        else:
            return "Invalid item type: %s" % item.type
    else:
        if product_amount > MAX_TOTAL:
           return f"Total amount payable for an order exceeded: product_amount {product_amount}"
        elif payment_amount > MAX_TOTAL:
           return f"Total amount payable for an order exceeded: payment_amount {payment_amount}"

    if payment_amount - product_amount != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payment_amount - product_amount)
    else:
        return "Order ID: %s - Full payment received!" % order.id