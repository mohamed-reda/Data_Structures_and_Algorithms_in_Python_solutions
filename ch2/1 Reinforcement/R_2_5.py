# -----------R2.5-------------------
class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0  # Start with a balance of zero

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

    def charge(self, price):
        try:
            price = float(price)  # This will accept an int, float or string that can be converted to a float
        except:
            print('Invalid input')
            return False
        if price + self._balance > self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit() - self.get_balance()}')
            return False  # You are going over your limit
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        try:
            amount = float(amount)  # This will accept an int, float or string that can be converted to a float
        except:
            print('Invalid input')
            return False
        self._balance -= amount
        return True


cc1 = CreditCard('Andrew', 'ABC', '1234567890', 1000)
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

# # -----------R2.5-------------------
# class CreditCard():
#     def __init__(self, customer, bank, acnt, limit):
#         self._customer = customer
#         self._bank = bank
#         self._account = acnt
#         self._limit = limit
#         self._balance = 0  # Start with a balance of zero
# 
#     def get_customer(self):
#         return self._customer
# 
#     def get_bank(self):
#         return self._bank
# 
#     def get_account(self):
#         return self._account
# 
#     def get_limit(self):
#         return self._limit
# 
#     def get_balance(self):
#         return self._balance
# 
#     def set_balance(self, value):
#         self._balance = value
# 
#     def charge(self, price):
#         try:
#             price = float(price)  # This will accept an int, float or string that can be converted to a float
#         except:
#             print('Invalid input')
#             return False
#         if price + self._balance > self._limit:
#             print(f'Your deposit of {price} exceeds your remainder of {self.get_limit() - self.get_balance()}')
#             return False  # You are going over your limit
#         else:
#             self._balance += price
#             return True
# 
#     def make_payment(self, amount):
#         try:
#             amount = float(amount)  # This will accept an int, float or string that can be converted to a float
#         except:
#             print('Invalid input')
#             return False
#         self._balance -= amount
#         return True
# 
# 
# cc1 = CreditCard('Andrew', 'ABC', '1234567890', 1000)
# cc1.make_payment(100);
# print(cc1.get_balance())
# cc1.charge(100);
# print(cc1.get_balance())
# cc1.charge(500);
# print(cc1.get_balance())
# cc1.charge(200);
# print(cc1.get_balance())
# cc1.charge(100);
# print(cc1.get_balance())
# cc1.charge(500);
# print(cc1.get_balance())
# cc1.charge("Hello");
# print(cc1.get_balance())
# cc1.charge("20");
# print(cc1.get_balance())
# cc1.charge("453.4");
# print(cc1.get_balance()
