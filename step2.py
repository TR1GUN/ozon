

class Order:

    price = None
    number = None

    def __init__(self, number: str, price:float):
        self.number = number
        self.price = price

    def get_order(self):

        return {'number': self.number,
                'price': self.price}


from random import randint

count_order = 1000
bascket = []

for i in range(count_order):
    bascket.append(Order(number= str(i) , price= randint(1, 10000)).get_order())



bascket2  = []
for i in bascket:
    if i['price'] > 1000:
        bascket2.append(i)

from copy import deepcopy
total_price = 0
for i in bascket2:

    total_price = total_price + deepcopy(i['price'])
