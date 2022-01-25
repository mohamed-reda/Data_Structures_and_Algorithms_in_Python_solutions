from R_2_5 import CreditCard


class CreditCardSelfReport(CreditCard):
    def special_charge(self, amount):
        if super().charge(amount):
            return True
        else:
            print("Credit card has failed:", self.get_bank())


wallet = []
wallet.append(CreditCardSelfReport('John Bowman', 'California Savings', '56 5391 0375 9387 5309', 2500))
wallet.append(CreditCardSelfReport('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
wallet.append(CreditCardSelfReport('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))

for val in range(1, 100):
    wallet[0].special_charge(val)
    wallet[1].special_charge(2 * val)
    wallet[2].special_charge(3 * val)

for c in range(3):
    print('Customer = ', wallet[c].get_customer())
    print('Bank = ', wallet[c].get_bank())
    print('Account = ', wallet[c].get_account())
    print('Limit = ', wallet[c].get_limit())
    print('Balance = ', wallet[c].get_balance())
    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print('New Balance = ', wallet[c].get_balance())
    print()
