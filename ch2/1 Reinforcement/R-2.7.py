# --------------R2.7--------------------------
# Note, you must run the cell in R2-4 for this one to work
class CreditCardWithBalance(CreditCard):
    def __init__(self, customer, bank, acnt, limit, balance=0):
        super().__init__(customer, bank, acnt, limit)
        self._balance = balance


cc1 = CreditCardWithBalance('Andrew', 'ABC', '1234567890', 1000, 50)
cc1.make_payment(100);
print(cc1.get_balance())
cc1.charge(100);
print(cc1.get_balance())
cc1.charge(500);
print(cc1.get_balance())
cc1.charge(200);
print(cc1.get_balance())
cc1.charge(100);
print(cc1.get_balance())
cc1.charge(500);
print(cc1.get_balance())
cc1.charge("Hello");
print(cc1.get_balance())
cc1.charge("20");
print(cc1.get_balance())
cc1.charge("453.4");
print(cc1.get_balance())
