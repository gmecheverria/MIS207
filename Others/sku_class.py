class SKU:

    next_sku_num = 0

    def __init__(self, description, cost, price):
        self._description = description
        self._cost = cost
        self._price = price
        self._sku_num = SKU.next_sku_num
        SKU.next_sku_num += 1

    def __str__(self):
        return f"SKU# = {self._sku_num}, Description = {self._description}, Cost = {self._cost}, Price = {self._price}"

