class Shop:
    def __init__(self,price):
        self.price=price
    def _add_money(self,money):
        self.price+=money
    def _discount(self,amd):
        self.price-=(self.price*amd)//100
        assert 0<=self.price and amd>=0
    def _get_price(self):
        return self.price
customer1=Shop(50)
customer1._add_money(100)
customer1._discount(-110)
print(customer1._get_price())
