#
# Alter and test a new coffee cup class that adds sip
# (which takes a drink of 0.5 ounce), and gulp (which takes a drink of 2 ounces)
#

class Cup:
    def __init__(self, size):
        self._size = size
        self._amount = 0
    def fill(self):
        self._amount = self._size
    def drink(self, amount=1):
        ret_amount = 0
        if self._amount >= amount:
            self._amount -= amount
            ret_amount = amount
        else:
            ret_amount = self._amount
            self._amount = 0
        return ret_amount
    def sip(self, amount=0.5):
        ret_amount = 0
        if self._amount >= amount:
            self._amount -= amount
            ret_amount = amount
        else:
            ret_amount = self._amount
            self._amount = 0
        return ret_amount

    def gulp(self, amount=2):
        ret_amount = 0
        if self._amount >= amount:
            self._amount -= amount
            ret_amount = amount
        else:
            ret_amount = self._amount
            self._amount = 0
        return ret_amount

    def empty(self):
        self._amount = 0
    def getSize(self):
        return self._size
    def getAmount(self):
        return self._amount