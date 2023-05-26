class CashRegister:

    total_sales = 0

    def __init__(self, till = 0):
        self._till = till
        self._current_sale = 0
        self._current_count = 0

    def __str__(self):
        return f"Current sale = {self._current_sale} - total items = {self._current_count} - Amount in till = {self._till}"

    def add_item(self, total, count):
        self._current_count += count
        self._current_sale += total*count

    def get_total(self):
        return self._current_sale

    def clear(self):
        self._till += self._current_sale
        CashRegister.total_sales += self._current_sale
        self._current_sale = 0
        self._current_count = 0

