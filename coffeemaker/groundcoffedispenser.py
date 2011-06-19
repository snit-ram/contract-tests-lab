class GroundCoffeeDispenser(object):
    _amount = 0
    _led = None
    _min = 5

    def __init__(self, led):
        self._led = led
        self._led.on()

    def has(self, amount):
        return self._amount >= amount

    def get(self, amount):
        self._amount -= amount

        if self._amount < self._min:
            self._led.on()

        return 'groundcoffee', amount

    def fill(self, amount):
        self._amount += amount

        if self._amount >= self._min:
            self._led.off()