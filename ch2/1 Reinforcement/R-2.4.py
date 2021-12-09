class Flower():
    def __init__(self, name=None, petals=None, price=None):
        self._name = self._petals = self._price = None

        self.set_name(name)
        self.set_petals(petals)
        self.set_price(price)

    def set_name(self, name):
        try:
            self._name = str(name)
        except:
            print('Invalid input for a name, it must be a string')

    def set_petals(self, petals):
        try:
            self._petals = petals
        except:
            print('Invalid input')

    def set_price(self, price):
        if price is not None:
            try:
                self._price = float(price)
            except:
                print('Invalid price, must be a number (no dollar sign)')

    def get_name(self):
        if self._name is None:
            return ('Attribute has not been set')
        else:
            return self._name

    def get_price(self):
        if self._price is None:
            return ('Attribute has not been set')
        else:
            return self._price

    def get_petals(self):
        if self._petals is None:
            return ('Attribute has not been set')
        else:
            return self._petals


Dand = Flower('Dandelion', 5, '$10.32')
print(Dand.get_name(), Dand.get_petals(), Dand.get_price())

print('\n')
Rose = Flower()
print(Rose.get_name(), Rose.get_petals(), Rose.get_price())

Rose.set_name('Rose')
Rose.set_price(20)
Rose.set_petals(30)
print(Rose.get_name(), Rose.get_petals(), Rose.get_price())
